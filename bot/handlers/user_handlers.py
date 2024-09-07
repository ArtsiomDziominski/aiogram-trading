from aiogram import types, Router, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from bot.keyboards.user_keyboards import get_main_kb

router = Router()

async def cmd_start(msg: Message) -> None:
    reply_text = f'To log in and start receiving notifications, enter /login and follow the instructions.'
    await msg.answer(text=reply_text, reply_markup=get_main_kb())


async def cmd_app(message: Message):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(
                text='Open app',
                web_app=WebAppInfo(url=f'https://anturium.vercel.app/main'),
            )
        ]]
    )
    await message.answer("app", reply_markup=markup)


def register_user_handlers(dp: Dispatcher) -> None:
    dp.message.register(cmd_start, Command(commands=["start"]))
    dp.message.register(cmd_app, Command(commands=["app"]))
