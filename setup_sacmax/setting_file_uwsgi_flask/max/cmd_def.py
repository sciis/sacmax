#!/usr/bin/python
#coding: utf-8

import imp
general_def = imp.load_source('general_def', '/home/pi/general.conf')

# コマンドの定義
COMMAND_PROP = {
    'test_sacmax':[general_def.HELLO_PORT],
    'pin12_on':[general_def.GPIO_PORT],
    'pin12_off':[general_def.GPIO_PORT],
    'pin12_stat':[general_def.GPIO_PORT]
}
