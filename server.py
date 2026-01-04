import asyncio
import websockets

clients = set()

async def handler(ws):
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

async def main():
    print("Servidor WebSocket listo")
    async with websockets.serve(handler, "0.0.0.0", 8765):
        await asyncio.Future()

asyncio.run(main())
