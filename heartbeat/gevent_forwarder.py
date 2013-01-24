from gevent import spawn
from gevent_zeromq import zmq

class GEForwarder(object):
    def __init__(self, incoming, outgoing):
        self.incoming = incoming
        self.outgoing = outgoing

        context = zmq.Context()
        self.incoming_socket = context.socket(zmq.SUB)
        self.incoming_socket.bind(self.incoming)
        self.incoming_socket.setsockopt(zmq.SUBSCRIBE, "")

        self.outgoing_socket = context.socket(zmq.PUB)
        self.outgoing_socket.bind(self.outgoing)
    
