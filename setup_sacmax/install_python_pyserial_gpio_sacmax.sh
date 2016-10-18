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
    
    #gpio
     pip3 install RPI.GPIO
     echo "GPIO OK!"
    #pyserial
     pip3 install pyserial
     echo "pyserial OK!"
}

case "$1" in
    install)
    do_install
    echo "installed!"
    ;;

    *)
    echo "-------------WARNING!-------------"
    echo "  Mistake in your input." 
    echo "  If you try this shell, you can"
    echo "select these commands"
    echo "  1.install" 
    exit 1
    ;;
esac


#end