#!bin/bash

do_start(){
    sh /etc/init.d/nginx start
    sh /etc/init.d/uwsgi start
    echo "started!"
}

do_stop(){
    sh /etc/init.d/nginx stop
    sh /etc/init.d/uwsgi stop
    echo "stoped!"
}

#if don't printed" [uWSGI] getting INI configuration ...", Please try stop and start command.
do_restart(){
    #sh /etc/init.d/nginx restart
    #sh /etc/init.d/uwsgi restart
    do_stop
    echo "please wait..."
    sleep 3
    echo "restart"
    do_start
    echo "restarted!"
}

case "$1" in
    start)
    do_start
    ;;
    stop)
    do_stop
    ;;
    restart)
    do_restart
    ;;
    *)
    echo "-------------WARNING!-------------"
    echo "  Mistake in your input." 
    echo "  If you try this shell, you can"
    echo "select these commands"
    echo "(start/stop/restart)" 
    exit 1
    ;;
esac

#end