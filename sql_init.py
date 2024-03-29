"""Инициализация таблиц MySQL"""
import aiomysql
from decouple import config
from aiomysql.cursors import DictCursor


async def db_table_check() -> None:
    async with aiomysql.connect(
        host=config('IP_MYSQL', default=''),
        user=config("SQL_USR_ID", default=''),
        password=config('SQL_PASS', default=''),
        db=config('SQL_DB', default=''),
        charset='utf8mb4',
        cursorclass=DictCursor  # Курсор будет возвращать значения в виде словарей

    ) as connection:
        async with connection.cursor() as cur:
            pass
