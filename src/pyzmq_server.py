import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind('tcp://*:5555')

# Need to change the server code to eventually send some message
while True:
    message = socket.recv(copy=False)
    socket.send(b"World")
