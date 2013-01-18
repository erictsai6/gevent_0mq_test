import config

import argparse, sys
parser = argparse.ArgumentParser()
parser.add_argument("--type", choices=["server", "client"], required=True)
parser.add_argument("--threading", choices=["gevent", "native"], default="gevent")
parsed_arguments = parser.parse_args(sys.argv[1:])

if parsed_arguments.threading == "gevent":
    from gevent_zeromq import zmq
    import gevent
    from af_thread.gevent_server import GEServer
    from af_thread.gevent_client import GEClient

def gevent_start_server_client():
    gevent_list = []
    if parsed_arguments.type == "client":
        for n in range(0, config.NUM_THREAD):
            ge_client = GEClient(config.HOST, config.PORT_START+n)
            gevent_list.append(gevent.spawn(ge_client.receive))
    else:
        for n in range(0, config.NUM_THREAD):
            print n
            try:
                ge_server = GEServer(config.HOST, config.PORT_START+n)
                gevent_list.append(gevent.spawn(ge_server.serve))
            except Exception, e:
                print e
    return gevent_list

def main():
    if parsed_arguments.threading == "gevent":
        gevent_list = []
        gevent_list = gevent_start_server_client() 
        try:
            print "got here"
            gevent.joinall(gevent_list)
        except Exception, e:
            print e


if __name__ == "__main__":
    print "#" * 30
    print "Initialized 0MQ Threading Test type: {0}, threading: {1}".format(parsed_arguments.type, parsed_arguments.threading)
    print "#" * 30

    main()

    print "#" * 30
    print "Exiting..."
    print "#" * 30
    sys.exit(0)
