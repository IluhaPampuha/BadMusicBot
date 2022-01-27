from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button1 = KeyboardButton("/artists")
button2 = KeyboardButton("/songs")

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client.add(button1).insert(button2)
