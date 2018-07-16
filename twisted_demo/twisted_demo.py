#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
""""""

from twisted.internet import reactor
import time


def print_hello():
    print time.time()


def stop():
    reactor.stop()

print type(reactor)

reactor.callLater(6, print_hello)
reactor.callLater(10, stop)

reactor.run()
