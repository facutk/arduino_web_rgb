from flask import Flask
from werkzeug.contrib.cache import SimpleCache
from flask import render_template
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
    return render_template('index.html')

if __name__ == '__main__':
    cache.set('color', '000000')
    app.run()
