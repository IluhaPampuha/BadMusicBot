from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

button_user = InlineKeyboardButton(text="О себе", callback_data="user")
button_menu = InlineKeyboardButton(text="Меню", callback_data="menu")
button_help = InlineKeyboardButton(text="Помощь", callback_data="help")
button_download = InlineKeyboardButton(text="Загрузить", callback_data="download")

button_add = InlineKeyboardButton(text="Добавить в карзину", callback_data="add")

button_del = InlineKeyboardButton(text="Удалить товар", callback_data="del")


kb_menu = InlineKeyboardMarkup(row_width=2)
kb_menu_for_admin = InlineKeyboardMarkup(row_width=2)
kb_client = InlineKeyboardMarkup(row_width=1)
kb_admin = InlineKeyboardMarkup(row_width=2)

kb_menu.add(button_user).row(*[button_menu, button_help])
kb_menu_for_admin.add(button_user).row(*[button_menu, button_help, button_download])
kb_client.row(button_add)
kb_admin.row(*[button_add, button_del])
