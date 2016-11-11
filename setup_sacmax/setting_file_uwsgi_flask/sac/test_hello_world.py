# coding: utf-8

""" sacmax test code
"""

import time
import imp
import threading
import socket
import datetime
from queue import Queue

general_def = imp.load_source('general_def', '/home/pi/general.conf')

class HelloWorld:
    def __init__(self):
        self.sleep_time = 1

    def test_sacmax(self, q):        
        time.sleep(self.sleep_time)
        mesg = "Hello world. sacmax is here!"
        print(mesg)
        q.put(mesg)

if __name__ == '__main__':
    srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv_sock.bind((general_def.HOST, general_def.HELLO_PORT))
    srv_sock.listen(10)

    q = Queue()

    hello = HelloWorld()

    while True:
        cli_sock, cli_addr = srv_sock.accept()
        recv = cli_sock.recv(1024).decode('utf-8')
        print('%s: %s' % (__file__, recv))

        if recv != '':
            func = getattr(hello, recv)
            proc = None
            proc = threading.Thread(target=func, args=(q,))
            proc.start()
            mesg = q.get()
            reply = '%s,%s,%s' % (__file__.split('/')[-1], recv, mesg)
            cli_sock.sendall(reply.encode('utf-8'))
            recv = ''
            time.sleep(0.5)
