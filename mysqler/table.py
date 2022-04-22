# MySQLer - Table

from __future__ import annotations

from typing import TypeVar

from enum import Enum, auto


__all__ = ("ColumnType", "Table", "TableError")


class ColumnType(Enum):
    "Data type type."

    # 整数
    INT = auto
    TINYINT = auto
    MEDIUMINT = auto
    BIGINT = auto
    # 固定小数点型 
    DECIMAL = auto
    NUMERIC = auto
    # 浮動小数点型 
    FLOAT = auto
    DOUBLE = auto
    # ビット値
    BIT = auto
    # 時間
    DATE = auto
    DATETIME = auto
    TIMESTAMP = auto
    YEAR = auto
    # 文字列
    CHAR = auto
    BINARY = auto
    BLOB = auto
    TEXT = auto
    ENUM = auto
    SET = auto

    
class TableMeta(type):
    def __new__(cls, name, base, dct, **kwargs) -> TableMeta:
        columns = {}
        for name, type_ in dct.items():
            if isinstance(type_, ColumnType):
                columns[name] = type_.name
            elif isinstance(type_, str) and not name.startswith("__"):
                columns[name] = type_
        dct["table_name"] = kwargs.pop("table_name", name)
        dct["columns"] = columns
        return super().__new__(cls, name, base, dct)


class TableError(Exception):
    "This is an error that can occur when working with tables."


ValueT = TypeVar("ValueT")
class Table(metaclass=TableMeta):
    """Table Class.  
    This class is used by inheritance.  
    Then allows for easy SQL generation.

    Examples:
        ```python
        class FavoritefoodTable(Table):
            user = ColumnType.BIGINT
            food = ColumnType.TEXT

        table = FavoritefoodTable()

        table.select()
        # `SELECT * FROM FavoritefoodTable;`
        ```"""

    table_name: str
    "The name of the table."
    columns: dict[str, str]
    "Columns that is contained in the table."

    @property
    def create(self) -> str:
        "Generate sql of `CREATE TABLE`."
        return "CREATE TABLE IF NOT EXISTS {} ({})".format(
            self.table_name, ', '.join(f'{i} {self.columns[i]}' for i in self.columns)
        )

    def _exists(self, kwargs: dict):
        # 渡されたkwargsのキーでない列があった場合エラーを起こす。
        for name in kwargs:
            if name not in self.columns:
                raise TableError("Columns that do not exist.")

    def insert(self, **kwargs: ValueT) -> tuple[str, list[ValueT]]:
        """Execute `INSERT INTO`.

        Args:
            **kwargs: This is specified in the `WHERE`.

        Raises:
            TableError: If a column is not found"""
        self._exists(kwargs)
        return "INSERT INTO {} ({}) VALUES ({});".format(
            self.table_name, ", ".join(name for name in kwargs),
            ', '.join('%s' for _ in kwargs)
        ), list(kwargs.values())
    
    def select(self, targets_: str = "*", **kwargs: ValueT) -> tuple[str, list[ValueT]]:
        """Execute `SELECT ... FROM`.

        Args:
            targets_: A string that is placed after `SELECT`.
            **kwargs: This is specified in the `WHERE`.

        Raises:
            TableError: If a column is not found"""
        if kwargs == {}:
            return (f"SELECT {targets_} FROM {self.table_name};", [])
        else:
            self._exists(kwargs)
            return "SELECT {} FROM {} WHERE {};".format(
                targets_, self.table_name, " AND ".join(f"{name}=%s" for name in kwargs)
            ), list(kwargs.values())