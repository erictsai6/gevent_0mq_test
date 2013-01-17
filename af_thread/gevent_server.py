from gevent import spawn
from gevent_zeromq import zmq

class GEServer(object):
    def __init__(self, host, port):
        _tcp = "tcp://{0}:{1}".format(host, port)

        context = zmq.Context()

        self.address = _tcp
        self.host = host
        self.port = port
        self.server_socket = context.socket(zmq.REQ)
        self.server_socket.bind(_tcp)

    def serve(self):
        for n in range(0, 10):
            self.server_socket.send("random text from server")
            print "%s sending %s" % (self.port, n)
