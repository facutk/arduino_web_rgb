from flask import Flask
from werkzeug.contrib.cache import SimpleCache
from flask import send_file, jsonify
cache = SimpleCache()
app = Flask(__name__)

@app.route('/color/<param>')
def color(param):
    cache.set('color', param)
    return 'ok'

@app.route('/')
def index():
    #color = cache.get('color')
    #return '<body bgcolor="%s">'%(color)
    #return send_file('templates/index.html')
    return send_file('templates/index.html')

@app.route('/greeting')
def greeting():
    return jsonify( id = 1, content = 'dance with dragons' )

if __name__ == '__main__':
    cache.set('color', '000000')
    app.run()
