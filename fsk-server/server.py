from flask import Flask
from werkzeug.contrib.cache import SimpleCache
from flask import jsonify, request, send_file
cache = SimpleCache()
app = Flask(__name__)

@app.route('/color', methods=['GET', 'POST'])
def color():
    if request.method == 'POST':
        color = request.form['color']
        cache.set('color', color)
        return jsonify( status = 'ok', color = color )
    else:
        color = cache.get('color')
        return jsonify( status = 'ok', color = color )

@app.route('/')
def index():
    return send_file('templates/index.html')

if __name__ == '__main__':
    cache.set('color', '000000')
    app.run(host='0.0.0.0')
