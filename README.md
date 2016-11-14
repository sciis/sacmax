  
  
# sacmax.  
  Sensor, Actuator and Camera - easy to MAXimum.  
  
  
## Description  
  sacmax.により、RaspberryPiを使ったシステムの試作を効果的に進めることができます。またsacmax.は開発者がシステムの全貌を短時間で把握できるようPython3で簡潔に記述されており、構築したシステムの上に独自のアイデアを追加することも簡単です。  
  
#### カメラシステム
  ネットワーク監視カメラのような機能を短時間で構築したい場合には、sacmax.をお試しください。  
  sacmax.は画像の記録や、動画のストリーミング転送を実現するためのアプリを提供しています。内部にはOpenCVやGstreamer、MJPG-streamerといったOSSが使われており、これらの調査や習得にかかるコストを大幅に圧縮することができます。  
  関連するモジュールは以下のとおりです。  
  - sacmax_gst(Gstreamer1.0はGPLv2であることに注意してください)
  - sacmax_cv2
  
#### ラジコンカー
  ラジコンカーをスマートフォンで操縦したい場合には、sacmax.をお試しください。  
  sacmax.は、PWMによるモーター制御をWebブラウザ上で操作するためのアプリを提供しています。サイエンスパーク株式会社が販売する拡張ボードと組み合わせて使うことで、市販のラジコンカーをプロポを使うことなくスマートフォンで操縦することができるようになります。  
  関連するモジュールは以下のとおりです。  
  - sacmax_extra_board
  
#### IoTデバイス
  クラウドサーバと通信してスイッチのON/OFFを行うIoTデバイスを試作したい場合には、sacmax.をお試しください。  
  sacmax.は、MySQLサーバやFTPサーバからデータを取得するためのアプリを提供しています。また、わずかな改造でサーバへのデータのアップロードも可能となります。  
  関連するモジュールは以下のとおりです。
  - sacmax_with_server
  
##Requirement  
 Raspbian jessie lite (ver. September 2016)  
 Raspberry Pi 2  
  
  
##Usage  
 ・nginx+uwsgi+flask  
    インストール後に同一ネットワーク上のPCからブラウザで以下のアドレスにアクセス  
     http://(Raspberry Pi のIPアドレス)/  
    アクセス後、"Check uwsgi & Flask"のリンクをクリックし、flask_test_pageに遷移すれば成功です。  
  
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
  
  ここではsetup_sacmaxをzipファイル(setup_sacmax.zip)にした前提で説明をしています。PeaZipなど圧縮解凍アプリをご利用ください。またwin8以降の場合は新規作成から作成可能です。  
  
  1.setup_sacmax.zipファイルを /home/pi上にダウンロードしてください  
  2.$ unzip setup_sacmax.zip   
  3.$ cd setup_sacmax  
  4.$ sudo sh install_nginx_sacmax.sh install  
  5.$ sudo sh install_python_uwsgi_sacmax.sh install  
  6.$ sudo sh install_python_uwsgi_sacmax.sh setapp  
  7.$ sudo sh install_python_pyserial_gpio_sacmax.sh install  
  8.$ sudo reboot  
  
  
##Licence  
  
