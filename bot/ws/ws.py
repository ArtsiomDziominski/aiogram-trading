import websockets
import os
from dotenv import load_dotenv

class WebSocketClient:
    def __init__(self, uri):
        self.uri = uri
        self.connection = None

    async def connect(self):
        self.connection = await websockets.connect(self.uri)
        print(f"Connected to {self.uri}")

    async def send_message(self, message):
        if self.connection:
            await self.connection.send(message)
        else:
            print("Connection is not established.")

    async def receive_message(self):
        if self.connection:
            message = await self.connection.recv()
            return message
        else:
            print("Connection is not established.")
            return None

    async def close(self):
        if self.connection:
            await self.connection.close()
            print("Connection closed.")
        else:
            print("Connection is not established.")

load_dotenv()
ws_client = WebSocketClient(os.getenv("WS_NOTIFICATION"))