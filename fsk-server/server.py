from flask import Flask
from werkzeug.contrib.cache import SimpleCache
from flask import jsonify, request, send_file
import serial
cache = SimpleCache()
app = Flask(__name__)
ser = serial.Serial('/dev/ttyUSB0', 9600)

def send_value( value ):
    char = str( chr( value ) )
    ser.write( char )

def rgb_to_6bit( rgb ):
    return int('00' + bin(int(rgb[0:1], 16))[2:].zfill(4)[0:2]
                + bin(int(rgb[2:3], 16))[2:].zfill(4)[0:2]
                + bin(int(rgb[4:5], 16))[2:].zfill(4)[0:2], 2)

@app.route('/color', methods=['GET', 'POST'])
def color():
    if request.method == 'POST':
        color = request.form['color']
        cache.set('color', color)
        send_value( rgb_to_6bit( color ) )
        return jsonify( status = 'ok', color = color )

@app.route('/')
def index():
    return send_file('templates/index.html')

if __name__ == '__main__':
    cache.set('color', '000000')
    app.run(host='0.0.0.0')
