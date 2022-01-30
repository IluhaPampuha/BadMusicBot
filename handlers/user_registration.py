from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

from data_base.sqlite_db import sql_add_user_command, check_user


class FSMUser(StatesGroup):
    user_id = State()
    name = State()
    address = State()
    phone_number = State()


# Проверяем есть ли пользователь в БД, стартуем машину состояний, передаем ID.
async def user_start(callback: types.CallbackQuery, state: FSMContext):
    if await check_user(callback.from_user.id):
        await FSMUser.name.set()
        async with state.proxy() as data:
            data["user_id"] = callback.from_user.id
        await callback.message.answer("Вам необходимо заполнить информацию о себе. Для начала укажите свое имя:")
        await callback.answer()


# Отмена сосотяния
async def cancel_state(message: types.Message, state: FSMContext):
    if await state.get_state() is None:
        return
    await state.finish()
    await message.reply("Отмена состояния")


# Ловим первый ответ пользователя
async def load_name_user(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
    await FSMUser.next()
    await message.answer(
        "Теперь введите адрес доставки в формате \n<b>г.Одинцово, Можайское шоссе, д. X, кв. X</b>:", parse_mode="html")


# Ловим второй ответ пользователя
async def load_address_user(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["address"] = message.text
    await FSMUser.next()
    await message.answer("Введите номер телефона в формате \n<b>+79XXXXXXXXX:</b>", parse_mode="html")


# Ловим третий ответ пользователя
async def load_number_user(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["phone_number"] = message.text
    await sql_add_user_command(state)
    await state.finish()
    await user_start(message, state)


def register_handler_registration_user(dp: Dispatcher):
    dp.register_callback_query_handler(user_start, text="user", state=None)
    dp.register_message_handler(cancel_state, state="*", commands=["Отмена2"])
    dp.register_message_handler(cancel_state, Text(equals="Отмена2", ignore_case=True), state="*")
    dp.register_message_handler(load_name_user, state=FSMUser.name)
    dp.register_message_handler(load_address_user, state=FSMUser.address)
    dp.register_message_handler(load_number_user, state=FSMUser.phone_number)
