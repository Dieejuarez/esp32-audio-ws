import asyncio
import websockets

PORT = 8765
clients = set()

async def handler(ws):
    print("Cliente conectado")
    clients.add(ws)
    try:
        async for msg in ws:
            for c in clients:
                if c != ws:
                    await c.send(msg)
    except:
        pass
    finally:
        clients.remove(ws)
        print("Cliente desconectado")

async def main():
    print("Servidor WS listo en puerto", PORT)
    async with websockets.serve(handler, "0.0.0.0", PORT):
        await asyncio.Future()

asyncio.run(main())
