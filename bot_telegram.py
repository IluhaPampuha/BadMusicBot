from aiogram.utils import executor
from create_bot import dp
from handlers import client, other, admin


async def on_startup(_):
    print("Бот вышел в онлайн")


admin.register_handler_admin(dp)
client.register_handler_client(dp)
other.register_handler_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
