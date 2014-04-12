#arduino_web_rgb
=======

##Description
Server to send colors to Arduino via serial interface.

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
* Browse to http://<IP>:5000
