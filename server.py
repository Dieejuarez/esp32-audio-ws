import asyncio
import websockets
import os
from aiohttp import web

PORT = int(os.environ.get("PORT", 8080))
ws_clients = set()

# ---------- WEBSOCKET ----------
async def ws_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    ws_clients.add(ws)
    print("WebSocket conectado")

    async for msg in ws:
        pass

    ws_clients.remove(ws)
    print("WebSocket desconectado")
    return ws

# ---------- HTTP AUDIO ----------
async def audio_handler(request):
    data = await request.read()

    for ws in ws_clients:
        if not ws.closed:
            await ws.send_bytes(data)

    return web.Response(text="OK")

# ---------- MAIN ----------
app = web.Application()
app.router.add_get("/", ws_handler)
app.router.add_post("/audio", audio_handler)

print("Servidor HTTP+WS listo")
web.run_app(app, port=PORT)
