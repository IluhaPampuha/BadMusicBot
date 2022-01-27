from aiogram import types, Dispatcher

from create_bot import bot
from keyboards import kb_client


async def command_start_and_help(message: types.Message):
    try:
        await bot.send_message(message.from_user.id,
                               "Добрый день, для поиска композиции необходимо выбрать тип поиска:",
                               reply_markup=kb_client)
    except:
        await message.reply("Общение с ботом через ЛС, напишите ему: @BadMusicBroBot")


async def artists(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Результат поиска по исполнителю")
    except:
        await message.reply("Общение с ботом через ЛС, напишите ему: @BadMusicBroBot")


async def songs(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Результат поиска по песне")
    except:
        await message.reply("Общение с ботом через ЛС, напишите ему: @BadMusicBroBot")


def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(command_start_and_help, commands=["start", "help"])
    dp.register_message_handler(artists, commands=["artists"])
    dp.register_message_handler(songs, commands=["songs"])
