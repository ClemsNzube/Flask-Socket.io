from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)

socketio = SocketIO(app)

@app.route("/")
def indexPage():
    return render_template("index.html")


@socketio.on('connect')
def connection():
    print("A user connected")

def ack():
    print("client recieved message succefully")


@socketio.on('message')
def handle_message(msg):
    send(msg, broadcast=True)

@socketio.on('disconnect')
def disconnection():
    print("A user disconnected")

if (__name__ == "__main__"):
    socketio.run(app, debug=True)