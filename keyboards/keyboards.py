from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

button_user = InlineKeyboardButton(text="Регистрация/О себе", callback_data="user")
button_menu = InlineKeyboardButton(text="Каталог", callback_data="catalog")
button_help = InlineKeyboardButton(text="Помощь", callback_data="help")

button_add = InlineKeyboardButton(text="Добавить в карзину", callback_data="add")
button_go_to_main_menu = InlineKeyboardButton(text="В главное меню", callback_data="go_to_main_menu")
button_download = InlineKeyboardButton(text="Загрузить", callback_data="download")

button_del = InlineKeyboardButton(text="Удалить товар", callback_data="del")

button_higirs = InlineKeyboardButton(text="Нигири", callback_data="nigirs")
button_gunkans = InlineKeyboardButton(text="Гунканы", callback_data="gunkans")
button_mini_rolls = InlineKeyboardButton(text="Мини роллы", callback_data="mini_rolls")
button_rolls = InlineKeyboardButton(text="Роллы", callback_data="rolls")
button_baked_rolls = InlineKeyboardButton(text="Запеченные роллы", callback_data="baked_rolls")
button_tempurs_rolls = InlineKeyboardButton(text="Темпура роллы", callback_data="tempurs_rolls")

kb_menu = InlineKeyboardMarkup(row_width=2).add(button_user).row(*[button_menu, button_help])
kb_menu_for_admin = InlineKeyboardMarkup(row_width=2).add(button_user).row(*[button_menu, button_help, button_download])
kb_catalog = InlineKeyboardMarkup(row_width=1).add(
    *[button_higirs, button_gunkans, button_mini_rolls, button_rolls, button_baked_rolls, button_tempurs_rolls])
kb_client = InlineKeyboardMarkup(row_width=2).row(*[button_add, button_menu]).add(button_go_to_main_menu)
kb_admin = InlineKeyboardMarkup(row_width=2).row(*[button_add, button_menu ]).row(*[button_del, button_go_to_main_menu])
