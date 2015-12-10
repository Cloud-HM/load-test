import zmq
import resource
from locust import TaskSet, Locust, events, task

resource.setrlimit(resource.RLIMIT_NOFILE, (3000, 3000))

class ZeroMqClient(object):
    context = zmq.Context()

    def __init__(self, host):
        # `host` parameter must be of format -> ex: tcp://127.0.0.1:5555
        print "Host information %s" % host
        self.socket = ZeroMqClient.context.socket(zmq.REQ)
        self.socket.connect(host)

    def __del__(self):
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
    def on_start(self):
        self.client.ping()

    @task
    def ping(self):
        self.client.ping()


class MobileAppUser(ZeroMqLocust):
    task_set = UserBehavior
    min_wait = 2
    max_wait = 4
