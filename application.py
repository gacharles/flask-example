from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Hola mundo, ahora notificaciones a Teams'