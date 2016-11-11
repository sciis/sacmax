#coding: utf-8

import time
import imp
import threading
import socket
import datetime
import RPi.GPIO as GPIO
from queue import Queue

general_def = imp.load_source('general_def', '/home/pi/general.conf')

# 使用できるGPIOのピンはraspberry pi の公式をご確認ください
GPIO_PIN = 12

class GpioPowCtrl:
    def __init__(self):
        self.sleep_time = 1
        # mode
        # GPIO.BOARD : pin number
        # GPIO.BCM   : gpio number
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(GPIO_PIN, GPIO.OUT)

    def pin12_on(self, q):
        print("PIN12 ON ...")
        GPIO.output(GPIO_PIN, True)
        mesg = self.__gpio_status()
        q.put(mesg)

    def pin12_off(self, q):
        print("PIN12 OFF...")
        GPIO.output(GPIO_PIN, False)
        mesg = self.__gpio_status()
        q.put(mesg)

    def pin12_stat(self, q):
        print("PIN12 status is...")
        mesg = self.__gpio_status()
        q.put(mesg)

    def __gpio_status(self):
        if GPIO.input(GPIO_PIN) == 1:
            print("ON")
            return "ON"
        else:
            print("OFF")
            return "OFF"

    def clean_up(self):
        GPIO.cleanup()

if __name__ == '__main__':
    srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv_sock.bind((general_def.HOST, general_def.GPIO_PORT))
    srv_sock.listen(10)

    q = Queue()

    gpio = GpioPowCtrl()

    while True:
        cli_sock, cli_addr = srv_sock.accept()
        recv = cli_sock.recv(1024).decode('utf-8')
        print('%s: %s' % (__file__, recv))

        if recv != '':
            func = getattr(gpio, recv)
            proc = None
            proc = threading.Thread(target=func, args=(q,))
            proc.start()
            mesg = q.get()
            reply = '%s,%s,%s' % (__file__.split('/')[-1], recv, mesg)
            cli_sock.sendall(reply.encode('utf-8'))
            recv = ''
            time.sleep(0.5)
