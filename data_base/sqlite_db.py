import sqlite3
from create_bot import bot
from admins import admins



def sql_start():
    global base, cur
    base = sqlite3.connect("database.db")
    cur = base.cursor()
    if base:
        print("Data base connected OK!")
    base.execute("CREATE TABLE IF NOT EXISTS menu(img, name, description, price)")
    base.execute("CREATE TABLE IF NOT EXISTS admins(telegram_id PRIMARY KEY, activate)")
    cur.execute(f"INSERT OR IGNORE INTO admins(?,?), {admins}")
    cur.execute(f"UPDATE my_table SET age = 34 WHERE name='Karen'")
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute("INSERT INTO menu VALUES (?,?,?,?)", tuple(data.values()))
        base.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute("INSERT INTO menu VALUES (?,?,?,?)", tuple(data.values()))
        base.commit()


async def sql_read(message):
    for photo, name, description, price in cur.execute("SELECT * FROM menu").fetchall():
        await bot.send_photo(message.from_user.id, photo, f"<b>{name}</b>\nОписание: {description}\nЦена: {price}", parse_mode="html")
        await message.delete()
