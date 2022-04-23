# MySQLer - MySQL

from aiomysql import Pool

from .table import Table


__all__ = ("TablePlus",)


class TablePlus(Table):
    def __init__(self, pool: Pool):
        self.pool = pool
    
    async def create(self):
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(super().create)
    
    async def insert(self, **kwargs):
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(super().insert(**kwargs))
                
    async def select(self, **kwargs):
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(super().select(**kwargs))
