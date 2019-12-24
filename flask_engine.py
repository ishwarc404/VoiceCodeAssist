
from flask import Flask, render_template
from flask_socketio import SocketIO
import json
import time
data = {'user_name': 'Server', 'message': 'this is message came from the server'}
data = json.dumps(data)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

@app.route('/')
def sessions():
    return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    # for i in range(10):
    while(True):
        time.sleep(1)
        socketio.emit('my response', data, callback=messageReceived)


if __name__ == '__main__':
    socketio.run(app, debug=True)
