class TableManager:
    def __init__(self, tablename, **kwargs):
        self.tablename = tablename
        self.kwargs = kwargs

    @property
    def create(self):
        colum = {}
        for name in self.kwargs:
            nametype = self.kwargs[name]
            if isinstance(str(), nametype):
                colum[name] = "TEXT"
            elif isinstance(int(), nametype):
                colum[name] = "BIGINT"
        last = ", ".join(f"{name} {colum[name]}"
                         for name in colum)
        return f"CREATE TABLE {self.tablename} " + last

    def insert(self, **kwargs):
        colums = ", ".join(name for name in kwargs)
        values = [kwargs[name] for name in kwargs]
        valuetext = ', '.join('%s' for i in values)
        return f"INSERT INTO {self.tablename}({colums}) VALUES({valuetext})", values

    def select(self, **kwargs):
        if kwargs == {}:
            return f"SELECT * FROM {self.tablename}"
        else:
            text = " AND ".join(f"{name}=%s" for name in kwargs)
            return f"SELECT * FROM {self.tablename} WHERE {text}"
