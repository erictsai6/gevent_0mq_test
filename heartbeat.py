"""
  Using a central broker we are able to send heartbeats to all servers
"""

import config
import time

import argparse, sys
parser = argparse.ArgumentParser()
parser.add_argument("--type", options=["central", "node"], default="node")
parser.add_argument("--shard", required=True)
parsed_arguments = parser.parse_args(sys.argv[1:])

if parsed_arguments.threading == "gevent":
    import gevent
    from af_thread.gevent_server import GEServer
    from af_thread.gevent_client import GEClient

def gevent_start_server_client():
    gevent_list = []
    if parsed_arguments.type == "client":
        for n in range(0, config.NUM_THREAD):
            try:
                ge_client = GEClient(config.HOST, config.PORT_START+n)
                gevent_list.append(gevent.spawn(ge_client.receive))
            except Exception, e:
                err_print("%s, port:%s" % (e, config.PORT_START+n))
    else:
        for n in range(0, config.NUM_THREAD):
            try:
                ge_server = GEServer(config.HOST, config.PORT_START+n)
                gevent_list.append(gevent.spawn(ge_server.serve))
            except Exception, e:
                err_print("%s, port:%s" % (e, config.PORT_START+n))
    return gevent_list

def main():
    gevent_list = []
    gevent_list = gevent_start_server_client() 
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
    std_print("Initialized 0MQ Threading Test type: {0}, threading: {1}".format(parsed_arguments.type, parsed_arguments.threading))
    std_print("#" * 30)

    begin_t = (time.time())

    main()

    end_t = (time.time())

    std_print("Processed in %.4f seconds" % (end_t - begin_t))

    std_print("#" * 30)
    std_print("Exiting...")
    std_print("#" * 30)
    sys.exit(0)
