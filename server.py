import asyncio
import websockets

PORT = 8765
clients = set()

async def handler(websocket):
    print("Cliente conectado")
    clients.add(websocket)
    try:
        async for message in websocket:
            print("Datos recibidos:", len(message), "bytes")
            for c in clients:
                if c != websocket:
                    await c.send(message)
    except Exception as e:
        print("Error:", e)
    finally:
        clients.remove(websocket)
        print("Cliente desconectado")

async def main():
    print("Servidor WebSocket listo")
    async with websockets.serve(handler, "0.0.0.0", PORT):
        await asyncio.Future()

asyncio.run(main())
