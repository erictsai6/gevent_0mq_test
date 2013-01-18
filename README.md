Gevent and 0MQ Test
=========

Description
-------
The purpose of this is to test the performance of gevent and to learn how to use 
gevent and 0mq and create our own central distributed broker

This was run on 64-bit Ubuntu 10.04

Requirements
--------
0MQ
    prerequisites:
    <ul>
    <li>libtool</li>
    <li>autoconf</li>
    <li>automake</li>
    </ul>
gevent
    prerequisites:
    <ul>
    <li>libevent-dev</li>
    <li>python-all-dev</li>
    <li>greenlet</li>

pyzmq
gevent_zmq


Usage
--------
Edit the config file with the host and the number of instances you want running

    python main.py [--type {server/client}]

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

