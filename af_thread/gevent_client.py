from gevent import spawn
from gevent_zeromq import zmq

class GEClient(object):
    def __init__(self, host, port):
        _tcp = "tcp://{0}:{1}".format(host, port)
       
        context = zmq.Context()

        self.address = _tcp
        self.host = host
        self.port = port
        self.client_socket = context.socket(zmq.REP)
        self.client_socket.bind(_tcp)

    def receive(self):
        for n in range(0, 10):
            self.client_socket.recv()
            print "   %s receiving %s" % (self.port, n)            
            #self.client_socket.send("random text from server")
            
