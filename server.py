import asyncio
import websockets
import pyaudio

RATE = 48000
CHANNELS = 1
FORMAT = pyaudio.paInt16

p = pyaudio.PyAudio()
stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    output=True
)

async def handler(ws):
    print("ESP32 conectada")
    async for data in ws:
        stream.write(data)

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8080):
        print("Servidor WebSocket listo")
        await asyncio.Future()

asyncio.run(main())
