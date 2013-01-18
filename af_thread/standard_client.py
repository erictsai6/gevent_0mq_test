import threading
import zmq

class THClient(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

        context = zmq.Context()
        self.client_socket = context.socket(zmq.REP)
        self.running = True

    def run(self):
        while self.running:
            _tcp = self.queue.get()
            self.client_socket.connect(_tcp)     

            for n in range(0, 10):
                self.client_socket.recv()
                print "   %s receiving %s" % (_tcp, n)
                self.client_socket.send("random text from server")

            self.queue.task_done() 
            self.running = False
