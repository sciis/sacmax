#!/usr/bin/python
#coding: utf-8

import sys
import os
from subprocess import Popen, check_call, PIPE
import time
import imp
import signal
import socket

from cmd_def import COMMAND_PROP

general_def = imp.load_source('general_def', '/home/pi/general.conf')

## pkillで自分自身を止めてしまうのを防止
## The operation which prevents a stop of a process(pkill)
def proc_int(frame, signum):
    pass

## コマンドの実行
# 複数のコマンドを実行する場合はcommand1,command2,...と書く
# @param command コマンド
def exec_command(command):
    FNULL = open(os.devnull, 'w')
    ret = ''
    signal.signal(signal.SIGINT, proc_int)

    command_list = command.split(',')
    for command in command_list:

        cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cli.connect((general_def.HOST, COMMAND_PROP[command][0]))
        command = command.encode('utf-8')
        cli.send(command)
        ret += cli.recv(1024).decode('utf-8')

    return ret

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print (exec_command(sys.argv[1]))
