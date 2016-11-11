#!/usr/bin/python
#coding: utf-8
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import url_for

from dev_ctrl import *

import sys
sys.path.append("./model")

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

if __name__ == "__main__":
    app.run()
