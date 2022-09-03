import socketio

sio = socketio.Server(async_mode='eventlet')


@sio.event
def connect(sid, environ, auth):
    print('client connected: ', sid)


@sio.event
def disconnect(sid):
    print('client disconnected: ', sid)


@sio.on('test')
def send_test(sid, data):
    print(f'client {sid} sent a test: {data}')
    sio.emit('send_message', f'Hola grillo', room=sid)
