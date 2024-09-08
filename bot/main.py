# import logging
import json
import os

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher

from bot.ws.ws import ws_client
from bot.ws.ws_auth import get_ws_auth_message
from bot.ws.ws_grid_bot import get_ws_grid_bot_message
from handlers.user_handlers import register_user_handlers
from fsm.login import register_user_fsm

load_dotenv()
token = os.getenv("TOKEN_API")
bot = Bot(token=token)
dp = Dispatcher()

register_user_handlers(dp)
register_user_fsm(dp)

async def send_message_to_user(user_id: int, text: str):
    await bot.send_message(chat_id=user_id, text=text)

async def websocket_loop():
    await ws_client.connect()

    try:
        await ws_client.send_message(json.dumps({ 'msg': "Connected aiogram!" }))

        while True:
            response = await ws_client.receive_message()
            # print(f"Server response: {response}")
            res_json = json.loads(response)
            if 'type' in res_json and "tgUserId" in res_json:
                ws_message = ''
                match res_json['type']:
                    case 'NOTIFICATION_AUTH':
                        ws_message = get_ws_auth_message(res_json['data'])
                    case 'NOTIFICATION_BOT':
                        ws_message = get_ws_grid_bot_message(res_json['data'])
                    case 'ERROR_NOTIFICATION_POSITION_RISK':
                        pass
                if ws_message: await send_message_to_user(res_json['tgUserId'], ws_message)

    except KeyboardInterrupt:
        print("Interrupted by user.")
    finally:
        print('close')
        await ws_client.close()

async def main():
    websocket_task = asyncio.create_task(websocket_loop())
    await dp.start_polling(bot)
    await websocket_task()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())