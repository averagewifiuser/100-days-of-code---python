from sys import prefix
from flask import Flask

from .main.routes import main

from .extensions import *

def create_app():
    app = Flask(__name__)

    #initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    #register blueprints
    app.register_blueprint(main, url_prefix='/api')

    return app