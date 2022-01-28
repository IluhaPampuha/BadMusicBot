from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

buttonload = KeyboardButton("/Загрузить")
buttondelete = KeyboardButton("/Удалить")

kb_admin = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_admin.add(buttonload).insert(buttondelete)