from aiogram.utils import executor
from create_bot import dp
from handlers import client, other, admin
from data_base import sqlite_db


async def on_startup(_):
    sqlite_db.sql_start()


admin.register_handler_admin(dp)
client.register_handler_client(dp)
other.register_handler_other(dp)
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
