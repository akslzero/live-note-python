from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

text_data = ""  # Penyimpanan sementara di memori

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('text-change')
def handle_text_change(data):
    global text_data
    text_data = data
    emit('text-update', text_data, broadcast=True, include_self=False)

@socketio.on('request-text')
def handle_request_text():
    emit('text-update', text_data)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
