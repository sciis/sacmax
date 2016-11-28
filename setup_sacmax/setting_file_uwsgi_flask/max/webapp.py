#!/usr/bin/python
#coding: utf-8
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import url_for

import json
from collections import OrderedDict
from functools import partial
import re

from dev_ctrl import *

import sys, os
sys.path.append("./model")

conf_dir = "/home/pi/"

app = Flask(__name__)

##error hundrer
@app.route('/500')
def abort500():
    abort(500)
@app.errorhandler(500)
def error_handler(error):
    return render_template('500.html', msg=error), 500

#sample
@app.route('/')
@app.route('/sample')
def index():
    return render_template('sample_flask.html')

# control
@app.route('/device/<command>')
def dev_ctrl(command):
    # printはuwsgiのログに出力されます
    print ("command is %s\n" % (command))

    recv = exec_command(command)
    recv = recv.split(',')
    module_name = recv[0]
    func_name = recv[1]
    mesg = recv[2]
    return render_template('sample_sacmax.html', module_name=module_name, func_name=func_name, mesg=mesg)

# conf setting
#mesg = "Succeeded"/"Failed"

@app.route('/conf_edit/')
@app.route('/conf_edit/<conf_name>')
@app.route('/conf_edit/<conf_name>', methods=['POST'])
def conf_edit_file(conf_name="no_select"):
    filtering_file = "general.conf"
    mesg = None
    target_file = ""
    print_json_data=[]

    try:
        conf_str = request.form['conf_data']
        mesg = "write"
    except Exception as e:
        mesg = None

    try:
        target_file = conf_dir + conf_name
    except Exception as e:
        mesg = "not input config_file"

    if mesg == "write":
        try:
            conf_data = json.loads(conf_str, object_pairs_hook=OrderedDict)
            f= open(target_file, 'w')
            json.dump(conf_data, f, sort_keys=False, indent=4)
            print("file_write " + conf_name)
            f.close()
            mesg = "Succeeded"
        except Exception as e:
            mesg = "Failed"

    ## conf ファイル探査
    conf_list = []
    conf_files = os.listdir(conf_dir)
    for file in conf_files:
        if file != filtering_file and ".conf" in file:
            conf_list.append(file)

    ## ファイルが存在しない場合の例外処理
    conf_check_flag = 0
    for list in conf_list:
        if conf_name == list:
            conf_check_flag += 1
    if conf_check_flag == 0 and mesg == None:
        mesg = "no such conf_file \" %s \"" % conf_name

    try:
        f= open(target_file, 'r')
        json_data = json.load(f, object_pairs_hook=OrderedDict)
        print_json_data = json.dumps(json_data, indent=4)
        f.close()
    except Exception as e:
        print(e)
        print_json_data ="Cannot read file!"

    ## printはuwsgiのログに出力されます
    print ("[SETTING_DBG]%s : %s \n" % (conf_name, mesg))
    #print ("[SETTING_DBG2]%s : %s \n" % (conf_name, print_json_data))
    return render_template('setting_sacmax.html',mesg=mesg, conf_name=conf_name, conf_list = conf_list, json_data = print_json_data )

if __name__ == "__main__":
    app.run()
