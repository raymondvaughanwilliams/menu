from structure import app
from dotenv import load_dotenv
from flask_socketio import SocketIO
socketio = SocketIO(app)

if __name__ == '__main__':
    load_dotenv()
    socketio.run(app, debug=True)
    # app.run(debug=True)
