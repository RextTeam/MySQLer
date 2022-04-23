from aiomysql import connect
from mysqler.mysql import TablePlus, ColumnType
import asyncio

class FavoritefoodTable(TablePlus):
    user = ColumnType.BIGINT
    food = ColumnType.TEXT
    
async def main():
    conn = await connect(user="", password="", host="")
    async with conn.cursor() as cur:
        async with FavoritefoodTable(cur) as table:
            await table.insert(user=938194919392, food="steak")
            await table.select(user=938194919392)
            print(await table.fetchall())
        
asyncio.run(main())
