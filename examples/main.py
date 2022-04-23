import asyncio

from mysqler import Table, ColumnType
from aiomysql import connect

class FavoritefoodTable(Table):
    user = ColumnType.BIGINT
    food = ColumnType.TEXT
    
async def main():
    conn = await connect(host="127.0.0.1", password="", user="")
    async with conn.cursor() as cur:
        table = FavoritefoodTable()
        await cur.execute(table.create)
        await cur.execute(table.insert(user=938194919392, food="steak"))
        await conn.commit()
        await cur.execute(table.select(user=938194919392))
        print(await cur.fetchall())
        
    await conn.close()
    
asyncio.run(main())
