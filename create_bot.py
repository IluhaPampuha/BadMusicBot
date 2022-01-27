from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot(token="1809730071:AAFTpYASkJnj81yenfOjN2Ir_HH7j-o4a1M")
dp = Dispatcher(bot, storage=storage)
