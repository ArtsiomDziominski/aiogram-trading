# import logging
import os

from dotenv import load_dotenv
import threading
import asyncio
import websockets

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from handlers.user_handlers import register_user_handlers
from fsm.login import register_user_fsm

load_dotenv()
token = os.getenv("TOKEN_API")
bot = Bot(token=token)
dp = Dispatcher()

register_user_handlers(dp)
register_user_fsm(dp)

async def main():
    await dp.start_polling(bot)

# @dp.message()
# async def handle_message_for_broadcast(message: Message):
#     await bot.send_message(1127373465, 'message.text')


async def connect_and_communicate():
    uri = "ws://localhost:9061"  # Замените на ваш URI веб-сокета

    try:
        async with websockets.connect(uri) as websocket:
            print("Successfully connected to the server.")

            # Отправляем сообщение
            await websocket.send("Hello, server!")

            # Получаем ответ
            response = await websocket.recv()
            print(f"Received: {response}")

    except ConnectionRefusedError:
        print("Connection refused. Ensure the WebSocket server is running and the port is correct.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(connect_and_communicate())
    asyncio.run(main())