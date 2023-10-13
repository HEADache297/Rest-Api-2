import os
import asyncpg

DATABASE_URL = os.getenv('DATABASE_URL')

async def connect():
    conn = await asyncpg.connect(dsn=DATABASE_URL)
    return conn