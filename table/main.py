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
