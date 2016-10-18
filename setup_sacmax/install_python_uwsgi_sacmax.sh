#!/bin/bash

do_install(){
    #python3
    if test ! -e /usr/bin/python3; then
         echo "setup python3"
         apt-get install python3 -y
         apt-get install python3-pip -y

         apt-get install chkconfig
    else
         echo "python3 OK"
    fi

    #uwsgi
     echo "isntall uwsgi"
     pip3 install uwsgi
     echo "uwsgi OK"
    #flask
     echo "isntall flask"
     pip3 install flask
     echo "flask OK"
    
    #uwsgi move
     cp setting_file_uwsgi_flask/uwsgi /etc/init.d/
     echo "setting uwsgi init file"
    
     mkdir /var/log/uwsgi/
     
     #uwsgi nginx on
     chmod 755 /etc/init.d/nginx
     chmod 755 /etc/init.d/uwsgi
     chkconfig nginx on
     echo "nginx start up setting OK!"
     chkconfig uwsgi on
     echo "uwsgit start up setting OK!"
}

do_setapp(){
     cp -r setting_file_uwsgi_flask/sac /home/pi
     cp -r setting_file_uwsgi_flask/max /home/pi
     cp -r setting_file_uwsgi_flask/general.conf /home/pi     
     echo "setup sac max dir."
     chown pi:pi /home/pi/sac/ -R
     chown pi:pi /home/pi/max/ -R
     chown pi:pi /home/pi/general.conf
     echo "you can edit theres!"
     
}

do_check(){
    uwsgi --version
}

case "$1" in
    install)
    do_install
    ;;

    check)
    do_check
    ;;

    setapp)
    do_setapp
    ;;

    *)
    echo "-------------WARNING!-------------"
    echo "  Mistake in your input." 
    echo "  If you try this shell, you can"
    echo "select these commands"
    echo "  1.install" 
    echo "  2,check"
    echo "  2,setapp"
    exit 1
    ;;
esac

#end