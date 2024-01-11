from aiogram import Router, F, html
from aiogram.types import Message, CallbackQuery, InputMediaVideo, FSInputFile
from aiogram.filters import Command
import os

import keyboards
import text
import dir_explorer as ex

from bot import bot


router = Router()


@router.message(Command("start"))
async def start_handler(msg:Message):
    await msg.delete()
    await msg.answer(text=text.startText_1, reply_markup=keyboards.first)


@router.callback_query(F.data == "main_menu")
async def return_to_main_menu(clbk: CallbackQuery):
    ex.set_default()
    available = ex.get_dir_content()
    content = ""
    counter = 1
    for i in available:
        content += f"{counter} - {i}\n"
        counter += 1
    await clbk.message.delete()
    await clbk.message.answer("Добро пожаловать в корневую директорию! Доступный контент:\n\n" + content + "\n\nДля выбора файла/дирректории отправильте номер эллемента в чат. Отправить необъодимо только номер, без знаком препинаяи и т.д.",
                              reply_markup=keyboards.menu)


@router.callback_query(F.data == "prev")
async def return_to_prev(clbk: CallbackQuery):
    ex.return_to_prev()
    available = ex.get_dir_content()
    content = ""
    counter = 1
    for i in available:
        content += f"{counter} - {i}\n"
        counter += 1
    await clbk.message.delete()
    await clbk.message.answer("Вы успешно вернулись в корневую дирректорию.\nДостуаный контент:\n\n" + content + "\n\nДля выбора файла/дирректории отправильте номер эллемента в чат. Отправить необъодимо только номер, без знаком препинаяи и т.д.",
                              reply_markup=keyboards.menu)


@router.message()
async def open_file_dir(msg: Message):
    index = 0
    await msg.delete()
    try:
        index = int(msg.text) - 1
    except TypeError:
        await msg.answer("Некоректно введён индекс", reply_markup=keyboards.first)
    data = ex.get_dir_content()
    target = ""
    try:
        target = data[index]
    except IndexError:
        await msg.answer("Некоректно введён индекс", reply_markup=keyboards.first)

    if os.path.isfile(os.path.join(os.getcwd(), target)):
        await msg.answer("Ваш файл:",reply_markup=keyboards.menu)
        await msg.answer_document(ex.get_file(target))
    else:
        ex.move_to(target)
        data = ex.get_dir_content()
        content = ""
        counter = 1
        for i in data:
            content += f"{counter} - {i}\n"
            counter += 1
        await msg.answer(f"Вы перешли в дирректорию {os.getcwd()}.\nДоступный контент:\n\n{content}", reply_markup=keyboards.menu)
