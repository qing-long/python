from flask import Flask
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret key"
socketio = SocketIO(app)

@socketio.on('message')
def handle_message(message):
    send(message)

@socketio.on('json')
def handle_json(json):
    send(json, json=True)
    
@socketio.on('my event')
def handle_my_custom_event(json):
    emit('my response', json)

if __name__ == "__main__":
    socketio.run(app)