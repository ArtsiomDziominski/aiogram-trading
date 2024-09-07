from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_main_kb() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Кнопка 1', callback_data='cb_btn_1_main')],
        [InlineKeyboardButton(text='Кнопка 2', callback_data='cb_btn_2_main')]
    ])
    return keyboard
