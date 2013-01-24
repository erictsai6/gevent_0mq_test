Gevent and 0MQ Test
=========

Description
-------
The purpose of this is to test the performance of gevent and to learn how to use 
gevent and 0mq and create our own central distributed broker

I've also added in a heartbeat simulation to test the 0MQ PUB/SUB socket type connection

This was run on 64-bit Ubuntu 10.04

Requirements
--------
<ul>
<li>0MQ</li>
    prerequisites:
    <ul>
    <li>libtool</li>
    <li>autoconf</li>
    <li>automake</li>
    </ul>
<li>gevent</li>
    prerequisites:
    <ul>
    <li>libevent-dev</li>
    <li>python-all-dev</li>
    <li>greenlet</li>
    </ul>
    
<li>pyzmq</li>
<li>gevent_zmq</li>
</ul>


Usage
--------
There are two usage cases with this repository.

1.  Edit the config file with the host and the number of instances you want running. 

    python main.py [--type {server/client}] [--threading {gevent/native}]

<b>Arguments</b>
<ul>
  <li>@type - <i>REQUIRED</i> set to server or client</li>
  <li>@threading - defaults to "gevent"</li>
</ul>

2.  This usage case has a central forwarder that reads in heartbeats and publishes them to all the connected nodes

    python heartbeat.py [--type {forwarder/node}] [--shard XX]

<b>Arguments</b>
<ul>
  <li>@type - defaults to "node"</li>
  <li>@shard - only required for type "node", should be distinct integer</li>
</ul>

Where XX is a user inputted integer.  This is used to give an identity to the node.  Start up the forwarder first before starting up the nodes.  There is a 10 second sleep before the node starts sending heartbeats every 100ms so start up your node instances within those 10 seconds so that the node config dictionaries are synchronized.

Troubleshooting
-------
If you run into Too many open files error then you need to edit the open files limit set by the OS
In Ubuntu you can view it with the following command

    ulimit -a -H

or simply

    ulimit -n

To edit it in Ubuntu edit the /etc/security/limits.conf file and add in 

    * - nofile 350000

or some other high number.

