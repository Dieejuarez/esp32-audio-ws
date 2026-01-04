import asyncio
import websockets
import os  # Importante para leer las variables de Railway

clients = set()

async def handler(ws):
    clients.add(ws)
    try:
        async for msg in ws:
            # Reenviar el audio a todos los demás clientes
            for c in clients:
                if c != ws:
                    try:
                        await c.send(msg)
                    except:
                        pass
    except:
        pass
    finally:
        clients.remove(ws)

async def main():
    # Railway asigna un puerto dinámico. Si no existe, usamos 8080 por defecto.
    port = int(os.environ.get("PORT", 8080))
    
    print(f"Servidor WebSocket iniciado en el puerto: {port}")
    
    # IMPORTANTE: Escuchar en "0.0.0.0" y el puerto dinámico
    async with websockets.serve(handler, "0.0.0.0", port):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
