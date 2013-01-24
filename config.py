"""
   Configuration File
"""
HOST = "127.0.0.1"

NUM_THREAD = 100
PORT_START = 5000

INCOMING = "tcp://{0}:{1}".format(HOST, PORT_START)
OUTGOING = "tcp://{0}:{1}".format(HOST,PORT_START+1)

