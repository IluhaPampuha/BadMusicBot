from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from create_bot import bot
from data_base import sqlite_db
from global_settings import config
from keyboards.keyboards import kb_menu, kb_menu_for_admin, kb_catalog


async def command_start(message: types.Message):
    try:
        if str(message.from_user.id) in config.ADMINS:
            await bot.send_message(message.from_user.id,
                                   "Добрый день и добро пожаловать в \n&#127843;<b>SushiLime!</b>&#127843;Прежде чем перейти в каталог заполните данные о себе, далее нажмите на каталог, чтобы составить заказ.",
                                   reply_markup=kb_menu_for_admin, parse_mode="html")
        else:
            await bot.send_message(message.from_user.id,
                                   "Добрый день и добро пожаловать в <b>SushiLime!</b>\nПрежде чем перейти в каталог заполните данные о себе, далее нажмите на каталог, чтобы составить заказ.",
                                   reply_markup=kb_menu, parse_mode="html")
        await message.delete()
    except:
        await message.answer("Общение с ботом через ЛС, напишите ему: @SushiLimeBot")


async def command_help(callback: types.CallbackQuery):
    if str(callback.from_user.id) in config.ADMINS:
        await bot.send_message(callback.from_user.id, "Чтобы составить заказ Вам необходимо сначала пройти регистрацию, а затем перейти в пункт каталог.",
                               reply_markup=kb_menu_for_admin)
    else:
        await bot.send_message(callback.from_user.id, "Чтобы составить заказ Вам необходимо сначала пройти регистрацию, а затем перейти в пункт каталог.",
                               reply_markup=kb_menu)
    await callback.answer()


async def catalog(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, "Выберите категорию:", reply_markup=kb_catalog)
    await callback.answer()


async def menu(callback: types.CallbackQuery):
    await sqlite_db.sql_read_menu(callback, callback.data)


def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=["start"])
    dp.register_callback_query_handler(command_start, text="go_to_main_menu")
    dp.register_callback_query_handler(command_help, text="help")
    dp.register_callback_query_handler(catalog, text="catalog")
    dp.register_callback_query_handler(menu, text=["nigirs", "gunkans", "mini_rolls", "rolls", "baked_rolls",
                                                   "tempurs_rolls"])
