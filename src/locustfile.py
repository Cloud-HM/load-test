from locust import TaskSet, task, Locust, events
import zmq


class ZeroMqClient(object):
    def __init__(self, address, **kwargs):
        print("Received address: {address}".format(address=address))
        self.address = address
        self.setup()

    def setup(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect("tcp://{address}".format(address=self.address))

    def ping(self):
        self.socket.send(b"Hello")
        message = self.socket.recv(copy=False)
        events.request_success.fire(
            request_type="zeromq",
            name="ping",
            response_time=100,
            response_length=0
        )
        print("Received reply [ {message} ]".format(message=message))


class MobileAppUser(Locust):
    address = "tcp://127.0.0.1:5555"
    min_wait = 325
    max_wait = 750

    def __init__(self, *args, **kwargs):
        super(Locust, self).__init__(*args, **kwargs)
        self.client = ZeroMqClient(self.host)

    class UserBehavior(TaskSet):
        @task(1)
        def ping(self):
            self.client.ping()
