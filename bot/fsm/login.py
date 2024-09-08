import json

from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from bot.ws.ws import ws_client

dp = Dispatcher()

class Reg(StatesGroup):
    jwt = State()

async def cmd_login_jwt(msg: Message, state: FSMContext) -> None:
    await state.set_state(Reg.jwt)
    await msg.answer('Укажите jwt')

@dp.message(Reg.jwt)
async def cmd_login_jwt_finally(msg: Message, state: FSMContext) -> None:
    await state.update_data(jwt=msg.text)
    data = await state.get_data()
    ws_message_authorization = {
        'authorization': data['jwt'],
        'type': 'TELEGRAM',
        'userId': msg.from_user.id
    }
    await ws_client.send_message(json.dumps(ws_message_authorization))
    await msg.answer(f'{data}')
    await state.clear()

def register_user_fsm(dp: Dispatcher) -> None:
    dp.message.register(cmd_login_jwt, Command(commands=["login_jwt"]))
    dp.message.register(cmd_login_jwt_finally, Reg.jwt)
