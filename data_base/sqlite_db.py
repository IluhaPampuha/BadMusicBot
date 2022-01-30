import sqlite3
from create_bot import bot
from keyboards.keyboards import kb_client, kb_admin, kb_menu
from global_settings import config


def sql_start():
    global base, cur
    base = sqlite3.connect("database.db")
    cur = base.cursor()
    if base:
        print("Data base connected OK!")
    base.execute("CREATE TABLE IF NOT EXISTS menu(img, name, description, price)")
    base.execute("CREATE TABLE IF NOT EXISTS users(user_id PRIMARY KEY, name, address, phone_number)")
    base.commit()


async def sql_add_in_menu_command(state):
    async with state.proxy() as data:
        cur.execute("INSERT INTO menu VALUES (?,?,?,?)", tuple(data.values()))
        base.commit()


async def sql_add_user_command(state):
    async with state.proxy() as data:
        cur.execute("INSERT INTO users VALUES (?,?,?,?)", tuple(data.values()))
        base.commit()


async def sql_read(callback):
    if str(callback.from_user.id) in config.ADMINS:
        for photo, name, description, price in cur.execute("SELECT * FROM menu").fetchall():
            await bot.send_photo(callback.from_user.id, photo, f"<b>{name}</b>\nОписание: {description}\nЦена: {price}",
                                 parse_mode="html", reply_markup=kb_admin)
    else:
        for photo, name, description, price in cur.execute("SELECT * FROM menu").fetchall():
            await bot.send_photo(callback.from_user.id, photo, f"<b>{name}</b>\nОписание: {description}\nЦена: {price}",
                                 parse_mode="html", reply_markup=kb_client)
        await callback.answer()


async def check_user(id):
    user_info = cur.execute("SELECT * FROM users WHERE user_id == ?", (id,)).fetchone()
    if user_info:
        await bot.send_message(id,
                               f"&#128525;\nИмя: <b>{user_info[1]}</b>\nАдрес: <b>{user_info[2]}</b>\nНомер телефона: <b>{user_info[3]}</b>",
                               parse_mode="html", reply_markup=kb_menu)
        return False
    else:
        return True


async def sql_read_admin(message):
    for photo, name, description, price in cur.execute("SELECT * FROM menu").fetchall():
        await bot.send_photo(message.from_user.id, photo, f"<b>{name}</b>\nОписание: {description}\nЦена: {price}",
                             parse_mode="html")
        await message.delete()
