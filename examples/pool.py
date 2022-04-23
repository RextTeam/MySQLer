from aiomysql import create_pool
from mysqler.mysql import TablePlus, ColumnType
import asyncio

class FavoritefoodTable(TablePlus):
    user = ColumnType.BIGINT
    food = ColumnType.TEXT

async def main():
    pool = await create_pool(user="", password="", host="")
    async with FavoritefoodTable(pool) as table:
        await table.insert(user=938194919392, food="steak")
        await table.select(user=938194919392)
        print(await table.fetchall())
        
asyncio.run(main())
