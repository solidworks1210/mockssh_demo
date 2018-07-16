#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
""""""

from twisted.internet import reactor, protocol


class QuickDisconnectedProtocol(protocol.Protocol):
    def __init__(self):
        pass

    def connectionMade(self):
        print"Connectedto:%s." % self.transport.getPeer().host
        self.transport.loseConnection()


class BasicClientFactory(protocol.ClientFactory):
    def __init__(self):
        pass

    protocol = QuickDisconnectedProtocol

    def clientConnectionLost(self, connector, reason):
        print'Lostconnection:%s' % reason.getErrorMessage()
        reactor.stop()

    def clientConnectionFailed(self, connector, reason):
        print'Connectionfailed: %s' % reason.getErrorMessage()
        reactor.stop()


reactor.connectTCP('www.baidu.com', 80, BasicClientFactory())
reactor.run()
