from locust import TaskSet, task, Locust, events
import zmq


class ZeroMqClient(object):
    context = zmq.Context()

    def __init__(self, address):
        self.socket = ZeroMqClient.context.socket(zmq.REQ)
        self.socket.connect("tcp://{address}".format(address=address))

    def __del__(self):
        if self.socket is not None:
            self.socket.close()

    def ping(self):
        self.socket.send(b"Hello")
        self.socket.recv(copy=False)
        events.request_success.fire(
            request_type="zeromq",
            name="ping",
            response_time=100,
            response_length=5
        )


class ZeroMqLocust(Locust):
    def __init__(self):
        super(ZeroMqLocust, self).__init__()
        self.client = ZeroMqClient(self.host)


class UserBehavior(TaskSet):
    @task(1)
    def ping(self):
        self.client.ping()


class MobileAppUser(ZeroMqLocust):
    task_set = UserBehavior
    min_wait = 325
    max_wait = 750
