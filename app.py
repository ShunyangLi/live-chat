from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/staff/', methods=["POST", "GET"])
def staff():
    return render_template('mul_chat.html')


@socketio.on('user post')
def handle_user_post(str, methods=['GET', 'POST']):
    socketio.emit('staff', str)


@socketio.on('staff post')
def handle_staff_post(str,  methods=['GET', 'POST']):
    user_id = str["user_id"]
    socketio.emit(user_id, str["user_message"])

@socketio.on('leave')
def handle_user_leave(str, methods=['GET', 'POST']):
    socketio.emit('leave', str["user_id"])


if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=80)