from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot(token="5274329187:AAFSCfLLhg9_cnuEcfYvj5wn61DaT54TIKs")
dp = Dispatcher(bot, storage=storage)
