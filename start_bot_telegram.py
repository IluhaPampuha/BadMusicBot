from aiogram.utils import executor
from create_bot import dp
from handlers import client, user_registration, admin
from data_base import sqlite_db


async def on_startup(_):
    sqlite_db.sql_start()


admin.register_handler_admin(dp)
client.register_handler_client(dp)
user_registration.register_handler_registration_user(dp)
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
