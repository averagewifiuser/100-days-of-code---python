from sys import prefix
from flask import Flask

from .main.routes import main

def create_app():
    app = Flask(__name__)

    app.register_blueprint(main, url_prefix='/api')

    return app