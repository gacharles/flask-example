from flask import Flask, render_template
application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/hello')
def hello_world():
    return 'Hola mundo, ahora notificaciones a Teams'