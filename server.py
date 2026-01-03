import asyncio
import websockets

async def audio_server(ws):
    print("ESP32 conectada")
    async for data in ws:
        print("Bytes:", len(data))

async def main():
    async with websockets.serve(audio_server, "0.0.0.0", 8080):
        await asyncio.Future()

asyncio.run(main())
