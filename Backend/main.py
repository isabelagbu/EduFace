from socketio import ASGIApp
from sockets.socket_manager import sio
import os
import uvicorn

app = ASGIApp(sio)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=int(os.environ.get('PORT', 3000)))