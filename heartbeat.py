"""
  Using a central broker we are able to send heartbeats to all servers

"""

import config
import time

import argparse, sys
parser = argparse.ArgumentParser()
parser.add_argument("--type", choices=["forwarder", "node"], default="node")
parser.add_argument("--shard" )
parsed_arguments = parser.parse_args(sys.argv[1:])

import gevent
from heartbeat.gevent_forwarder import GEForwarder
from heartbeat.gevent_node import GENode
import zmq

def gevent_start_forwarder_node():
    gevent_list = []
    if parsed_arguments.type == "node":
        if parsed_arguments.shard == None:
            err_print("No shard argument given, [--shard XX]")
        else:
            try:
                ge_node = GENode(config.OUTGOING, config.INCOMING, parsed_arguments.shard)
                gevent_list.append(gevent.spawn(ge_node.heartbeat))
                gevent_list.append(gevent.spawn(ge_node.listen_to_heartbeat))
            except Exception, e:
                err_print("%s" % (e))
    else:
        try:
            ge_forwarder = GEForwarder(config.INCOMING, config.OUTGOING)
            gevent_list.append(zmq.device(zmq.FORWARDER, ge_forwarder.incoming_socket, ge_forwarder.outgoing_socket))
        except Exception, e:
            err_print("%s" % (e))
    return gevent_list

def main():
    gevent_list = []
    gevent_list = gevent_start_forwarder_node() 
    try:
        gevent.joinall(gevent_list)
    except Exception, e:
        err_print(e)

def err_print(str):
    print "::ERROR::", str

def std_print(str):
    print str

if __name__ == "__main__":
    std_print("#" * 30)
    std_print("Initialized 0MQ Heartbeat Test type: {0}, shard (if applicable): {1}".format(parsed_arguments.type, parsed_arguments.shard))
    std_print("#" * 30)

    begin_t = (time.time())

    main()

    end_t = (time.time())

    std_print("Processed in %.4f seconds" % (end_t - begin_t))

    std_print("#" * 30)
    std_print("Exiting...")
    std_print("#" * 30)
    sys.exit(0)
