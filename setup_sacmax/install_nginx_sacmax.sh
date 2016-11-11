#!/bin/bash
#please  apt-get update


#nginx install and setting
#install nginx

do_install(){

    if test -e /usr/local/nginx/sbin/nginx; then
        echo "nginx OK"
        exit
    fi

    cd /
     mkdir build
    cd build

     wget http://nginx.org/download/nginx-1.9.3.tar.gz
     tar zxvf nginx-1.9.3.tar.gz

    cd nginx-1.9.3

     apt-get install libpcre3-dev libpcre++-dev libgd2-xpm-dev libgeoip-dev libxml2-dev libxslt-dev libssl-dev -y

    ./configure --prefix=/etc/nginx \
    --sbin-path=/usr/local/nginx/sbin/nginx \
    --conf-path=/etc/nginx/nginx.conf \
    --error-log-path=/var/log/nginx/error.log \
    --http-client-body-temp-path=/var/lib/nginx/body \
    --http-fastcgi-temp-path=/var/lib/nginx/fastcgi \
    --http-log-path=/var/log/nginx/access.log \
    --http-proxy-temp-path=/var/lib/nginx/proxy \
    --http-scgi-temp-path=/var/lib/nginx/scgi \
    --http-uwsgi-temp-path=/var/lib/nginx/uwsgi \
    --lock-path=/var/lock/nginx.lock \
    --pid-path=/var/run/nginx.pid \
    --with-pcre-jit \
    --with-debug \
    --with-http_addition_module \
    --with-http_dav_module \
    --with-http_geoip_module \
    --with-http_gzip_static_module \
    --with-http_image_filter_module \
    --with-http_realip_module \
    --with-http_stub_status_module \
    --with-http_ssl_module \
    --with-http_sub_module \
    --with-http_xslt_module \
    --with-ipv6 \
    --with-sha1=/usr/include/openssl \
    --with-md5=/usr/include/openssl 

     make
    # ./objs/nginx -V

     make install

     mkdir -p /var/lib/nginx/body
     mkdir -p /etc/nginx/conf.d/
     mkdir -p /etc/nginx/sites-enabled
     mkdir -p /etc/nginx/sites-available

    #nginx.conf move
    cd /home/pi/setup_sacmax
     cp setting_file_nginx/nginx.conf /etc/nginx/
    #init.d nginx move
     cp setting_file_nginx/nginx /etc/init.d/
    #link sacmax.conf
     cp setting_file_nginx/sacmax.conf /etc/nginx/sites-available
    ln -s /etc/nginx/sites-available/sacmax.conf /etc/nginx/sites-enabled/
    #www move
    cp -r setting_file_nginx/www /home/pi/
}

do_check(){
    /usr/local/nginx/sbin/nginx -V
}

case "$1" in
    install)
    echo "start install nginx!"
    do_install
    if test ! -e /usr/local/nginx/sbin/nginx; then
        echo "nginx OK!"
    fi
    ;;

    check)
    do_check
    ;;

    *)
    echo "-------------WARNING!-------------"
    echo "  Mistake in your input." 
    echo "  If you try this shell, you can"
    echo "select these commands"
    echo "  1.install" 
    echo "  2,check"
    exit 1
    ;;
esac

#end