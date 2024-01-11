from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup


first = [
    [InlineKeyboardButton(text="Дерево файлов", callback_data="main_menu")]
]
first = InlineKeyboardMarkup(inline_keyboard=first)

menu = [
    [InlineKeyboardButton(text="Главное меню", callback_data="main_menu")],
    [InlineKeyboardButton(text="Вернуться назад", callback_data="prev")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)


