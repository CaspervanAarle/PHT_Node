# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 17:13:32 2021

@author: Casper
"""

# NODE!

import socket
import pickle

HEADER = 30
FORMAT = 'utf-8'
#HOST = '192.168.0.13'    # Standard loopback interface address (localhost)
#PORT = 5050        # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class IPC_Server():
    def __init__(self, host, port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((host, int(port)))
            s.listen()
            conn, addr = s.accept()
            self.conn = conn
            self.addr = addr
            print('Aggregator connected with this locker from: ', addr)
        except:
            print("error occurred")


    def receive_request(self):
        msg_length = self.conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = self.conn.recv(msg_length)
            msg = pickle.loads(msg)
            return msg
        
    def respond(self, msg):
        message = pickle.dumps(msg)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        self.conn.send(send_length)
        self.conn.send(message)