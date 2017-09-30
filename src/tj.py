#!/usr/bin/env python

import socket
import threading
import logging
import os
import sys
import time

import configargparse
from googlesamples.assistant import auth_helpers

import audio
import action
import i18n
import speech
import tts

class Client(object):
    def __init__(self, actor, say, player):
        #Thread.__init__(self)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = None
        #replace with your ip
        self.sock.bind(("x.x.x.x", 5000))
        self.command = None
        self.actor = actor
        self.say = say
        self.player = player
        self.thread = threading.Thread(target=self.run, args=())
        self.thread.daemon = True
        self.thread.start()

    def run(self):
        while True:
            self.sock.listen(5)
            self.conn, self.addr = self.sock.accept()
            data = self.conn.recv(10240)
            string = data.decode("utf-8")
            print(string)
            self.actor.handle(string)
            

    def get_command(self):
        if self.command != None:
            return self.command
        else:
            return None

