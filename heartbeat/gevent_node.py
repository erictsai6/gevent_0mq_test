from gevent import spawn
from gevent_zeromq import zmq
from random import randint
import time

class GENode(object):
    def __init__(self, incoming, outgoing, shard):

        self.num_heartbeats = randint(25,75)
        print "Initalization of node %s, with num_heartbeats set to %s" % (shard, self.num_heartbeats)
        self.shard = shard
        
        self.incoming = incoming
        self.outgoing = outgoing

        context = zmq.Context()
        print "incoming"
        self.incoming_socket = context.socket(zmq.SUB)
        self.incoming_socket.connect(self.incoming)
        self.incoming_socket.setsockopt(zmq.SUBSCRIBE, "")

        print "outgoing"
        print self.outgoing
        self.outgoing_socket = context.socket(zmq.PUB)
        self.outgoing_socket.connect(self.outgoing)

        self.config = {}
   
    # Sends a random number of hearbeats
    def heartbeat(self):
        time.sleep(10)
        for n in range(0, self.num_heartbeats):
            msg = "%s" % (self.shard) 
            self.outgoing_socket.send(msg)

    
    # Listens for heartbeats and prints out configs
    def listen_to_heartbeat(self):
        while True:
            shard_id = self.incoming_socket.recv()
            if shard_id not in self.config:
                self.config[shard_id] = 0
            self.config[shard_id] += 1

            
            print self.config, "\n"
            



            
