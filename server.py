import asyncio
import websockets
import os

PORT = int(os.environ.get("PORT", 8765))
clients = set()

async def handler(websocket):
    print("Cliente conectado")
    clients.add(websocket)
    try:
        async for message in websocket:
            for c in clients:
                if c != websocket:
                    await c.send(message)
    except:
        pass
    finally:
        clients.remove(websocket)
        print("Cliente desconectado")

async def main():
    print("Servidor WebSocket listo en puerto", PORT)
    async with websockets.serve(handler, "0.0.0.0", PORT):
        await asyncio.Future()

asyncio.run(main())
