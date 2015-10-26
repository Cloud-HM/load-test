import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind('tcp://*:5555')

while True:
    message = socket.recv(copy=False)
    print("Received request: {message}".format(message=message))

    socket.send(b"World")
