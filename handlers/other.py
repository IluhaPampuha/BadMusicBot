import json
import string

from aiogram import types, Dispatcher


async def bannedlist(message: types.Message):
    if {i.lower().translate(str.maketrans("", "", string.punctuation)) for i in message.text.split()}.intersection(
            set(json.load(open("banlist.json")))) != set():
        await message.answer("Ругательства запрещены!")
        await message.delete()


def register_handler_other(dp: Dispatcher):
    dp.register_message_handler(bannedlist)
