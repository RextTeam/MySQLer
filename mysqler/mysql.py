# MySQLer - MySQL

from typing import Union

from aiomysql import Pool, Cursor, Connection

from .table import Table

import asyncio


__all__ = ("TablePlus",)


class TablePlus(Table):
    def __init__(self, pool_or_cursor: Union[Pool, Cursor]):
        self.pool_or_cursor = pool_or_cursor
        self.connection: Connection = None
        self.cursor: Cursor = None
        self.wait_event = None
        
    async def __aenter__(self):
        await self.connect()
        return self
    
    async def __aexit__(self, *args, **kwargs):
        await self.close()
    
    async def close(self):
        if isinstance(self.pool_or_cursor, Pool):
            self.pool.release(self.connection)
            self.connection = None
            self.cursor = None
            
    async def check(self):
        if self.connection is not None and self.cursor is not None:
            await self.wait_event.wait()
        
    async def connect(self):
        await self.check()
        if isinstance(self.pool_or_cursor, Cursor):
            self.cursor = self.pool_or_cursor
        else:
            self.connection = await self.pool.acquire()
            self.cursor = await self.connection.cursor()
            self.wait_event = asyncio.Event()
            
    async def execute(self, *args, **kwargs):
        if self.cursor is None:
            await self.wait_event.wait()
        else:
            await self.cursor.execute(*args, **kwargs)
            
    async def fetchall(self, *args, **kwargs):
        if self.cursor is None:
            await self.wait_event.wait()
        else:
            return await self.cursor.fetch_all(*args, **kwargs)
        
    async def fetchone(self, *args, **kwargs):
        if self.cursor is None:
            await self.wait_event.wait()
        else:
            return await self.cursor.fetch_all(*args, **kwargs)
    
    async def create(self):
        await self.execute(super().create)
    
    async def insert(self, **kwargs):
        await self.execute(super().insert(**kwargs))
                
    async def select(self, **kwargs):
        await self.execute(super().select(**kwargs))
