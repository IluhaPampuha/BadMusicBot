from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

from data_base.sqlite_db import sql_add_in_menu_command
from global_settings import config


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


# Старт админки
async def admin_start(callback: types.CallbackQuery):
    if str(callback.from_user.id) in config.ADMINS:
        await FSMAdmin.photo.set()
        await callback.message.reply("Загрузи фото")
        await callback.answer()
    else:
        await callback.message.answer("Вы не являетесь администратором!")
        await callback.answer()


# Отмена сосотяния
async def cancel_state(message: types.Message, state: FSMContext):
    if await state.get_state() is None:
        return
    await state.finish()
    await message.reply("Отмена состояния")


# Ловим первый ответ админа
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["photo"] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply("Теперь введите название")


# Ловим второй ответ админа
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
    await FSMAdmin.next()
    await message.reply("Введите описание")


# Ловим третий ответ админа
async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["description"] = message.text
    await FSMAdmin.next()
    await message.reply("Введите стоимость")


# Ловим последний ответ админа
async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data["price"] = float(message.text)
        except:
            await message.reply("Введите корректную стоимость")
            return load_price
    await sql_add_in_menu_command(state)
    await state.finish()


def register_handler_admin(dp: Dispatcher):
    dp.register_callback_query_handler(admin_start, text="download", state=None)
    dp.register_message_handler(cancel_state, state="*", commands=["Отмена"])
    dp.register_message_handler(cancel_state, Text(equals="Отмена", ignore_case=True), state="*")
    dp.register_message_handler(load_photo, content_types=["photo"], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
