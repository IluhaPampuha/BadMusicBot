from aiogram import types, Dispatcher

from create_bot import bot
from keyboards import kb_client
from data_base import sqlite_db


async def command_start_and_help(message: types.Message):
    try:
        await bot.send_message(message.from_user.id,
                               "Добрый день и добро пожаловать! Нажмите на меню, чтобы составить заказ.",
                               reply_markup=kb_client)
    except:
        await message.reply("Общение с ботом через ЛС, напишите ему: @BadMusicBroBot")


async def menu(message: types.Message):
    await sqlite_db.sql_read(message)



def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(command_start_and_help, commands=["start", "help"])
    dp.register_message_handler(menu, commands=["menu"])
