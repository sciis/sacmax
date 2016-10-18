#!/usr/bin/python
#coding: utf-8

import imp
general_def = imp.load_source('general_def', '/home/pi/general.conf')

# コマンドの定義
COMMAND_PROP = {
    'test_sacmax':[general_def.WEBCAM_PORT]
#sample
#    'wheel_mot_forward':[general_def.ROOMBA_PORT],
#    'wheel_mot_back':[general_def.ROOMBA_PORT],
#    'wheel_mot_left':[general_def.ROOMBA_PORT],
#    'wheel_mot_right':[general_def.ROOMBA_PORT],
#    'wheel_mot_stop':[general_def.ROOMBA_PORT],
#    'rmb_reset':[general_def.ROOMBA_PORT],
#    'rmb_stat':[general_def.ROOMBA_PORT],
#    'rmb_dock':[general_def.ROOMBA_PORT],
}
