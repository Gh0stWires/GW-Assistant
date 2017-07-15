#!/usr/bin/env python

import asyncore
import socket
import logging


class TJ(asyncore.dispatcher):

    def __init__(self, address):
        asyncore.dispatcher.__init__(self)
        self.logger = logging.getLogger('TJ')
        self.create_socket(socket.AF_INET,
                           socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(address)
        self.address = self.socket.getsockname()
        self.logger.debug('binding to %s', self.address)
        self.listen(5)


    def handle_connect(self):
        self.logger.debug('handle_connect()')
