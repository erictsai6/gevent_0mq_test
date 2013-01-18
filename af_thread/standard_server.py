import threading
import zmq

class THServer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

        context = zmq.Context()
        self.server_socket = context.socket(zmq.REQ)
        self.running = True

    def run(self):
        while self.running:
            _tcp = self.queue.get()
            self.server_socket.bind(_tcp)

            for n in range(0, 10):
                self.server_socket.send("random text from server")
                print "%s sending %s" % (_tcp, n)
                self.server_socket.recv()
            self.queue.task_done() 
            self.running = False
