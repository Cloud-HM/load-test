import zmq

context = zmq.Context()

print("Connecting to server...")
socket = context.socket(zmq.REQ)
socket.connect('tcp://localhost:5555')

for request in range(10):
    print("Sending request {request} ...".format(request=request))
    socket.send(b"Hello")

    message = socket.recv(copy=False)
    print("Received reply {request} [ {message} ]".format(request=request, message=message))