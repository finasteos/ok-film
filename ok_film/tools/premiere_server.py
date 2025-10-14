import http.server
import socketserver
import threading
import asyncio
import websockets

def http_server():
    PORT = 7331
    with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
        print(f"🎬 HTTP server for premiere at http://localhost:{PORT}")
        httpd.serve_forever()

async def chat_server(websocket, path):
    print("🎙️ Chat client connected")
    try:
        async for message in websocket:
            print(f"< {message}")
            # Placeholder for Gemini Live response
            response = f"Kimi hears you: '{message}' (live response)"
            await websocket.send(response)
            print(f"> {response}")
    except websockets.ConnectionClosed:
        print("👋 Chat client disconnected")

def websocket_server():
    start_server = websockets.serve(chat_server, "localhost", 8765)
    print(f"💬 WebSocket chat server running at ws://localhost:8765")
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    print("🚀 Starting OK Film Interactive Premiere Server...")
    
    # Run HTTP and WebSocket servers in separate threads
    http_thread = threading.Thread(target=http_server)
    ws_thread = threading.Thread(target=websocket_server)
    
    http_thread.daemon = True
    ws_thread.daemon = True
    
    http_thread.start()
    ws_thread.start()
    
    # Keep the main thread alive
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\n🛑 Shutting down servers.")