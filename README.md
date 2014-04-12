#arduino_web_rgb
=======

##Description
Server to send colors to Arduino via serial interface.

See it in action https://www.youtube.com/watch?v=uE0AGFHBTxQ
More information http://blog.facu.tk/2014/04/arduino-web-rgb.html


##Installation
* git clone https://github.com/facutk/arduino_web_rgb.git
* cd arduino_web_rgb
* virtualenv venv
* source venv/bin/activate
* pip install -r requirements.txt

##Usage
* Wire Arduino circuit and download firmware/arduino_web_rgb.ino
* Connect Arduino to computer via usb
* python fsk-server/server.py
* Browse to http://COMPUTER_IP:5000
