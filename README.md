

# sacmax.
  Sensor, Actuator and Camera - easy to MAXimum.


## Description
  sacmax を使用すると、webブラウザを介してwebカメラをコントロールすることが出来ます。またwebサーバのみセットアップすることもできます。そしてsacmaxを使用すると、そのカメラモジュールを簡単に作れます。つまり機能を考えることに使用者は集中することが出来ます。


##Requirement
 Raspbian jessie lite (ver. September 2016)
 Raspberry Pi 2


##Usage
 ・nginx+uwsgi+flask
    インストール後に同一ネットワーク上のPCからブラウザで以下のアドレスにアクセス
     http://(Raspberry Pi のIPアドレス)/

 ・sacmax(コマンドラインから動作確認)
     ターミナルを2つ開くなど、コマンドラインの画面を2つ用意してください(それぞれterminal_a、terminal_b とします)
     $ cd /home/pi/max
     terminal_a:
        $ python3 /home/pi/sac/test_hello_world.py
     terminal_b:
        $ python3 /home/pi/max/dev_ctrl.py test_sacmax

 ・sacmax(Webページから動作確認)
     コマンドラインから確認の terminal_a のコマンドを打ち込んでから、ブラウザのflask_test_page下にある"sacmax."のロゴをクリックしてください
     あるいは以下のurlにアクセスしてください
     http://(Raspberry Pi のIPアドレス)/device/test_sacmax


##Install

  ※IPアドレスのセットアップまでは終了させておいてください
  ※事前に sudo apt-get update をしておいてください

  1.setup_sacmax.zipファイルを /home/pi上にダウンロードしてください(zipしていなくとも、ダウンロード先は /home/pi です)
  2.$ unzip setup_sacmax.zip (zipしてインストールしていなければ不要です)
  3.$ cd setup_sacmax
  4.$ sudo sh install_nginx_sacmax.sh install
  5.$ sudo sh install_python_uwsgi_sacmax.sh install
  6.$ sudo sh install_python_uwsgi_sacmax.sh setapp
  7.$ sudo sh install_python_pyserial_gpio_sacmax.sh install
  8.$ sudo reboot


##Licence

