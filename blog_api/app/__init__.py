from sys import prefix
from flask import Flask

from .main.routes import main
from .users.routes import user

from .extensions import *
from .models import *

from .errorhandlers import *

def create_app():
    app = Flask(__name__)

    app.config.from_object('config.DevelopmentConfig')

    #initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    #register blueprints
    app.register_blueprint(main, url_prefix='/api')
    app.register_blueprint(user, url_prefix='/api/users')

    #registering errorhandlers
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(405, method_not_allowed)
    app.register_error_handler(500, internal_server_error)
    app.register_error_handler(403, forbidden)

    with app.app_context():
        @app.after_request
        def after_request(response):
            header = response.headers
            header['Access-Control-Allow-Origin'] = '*'
            header['Access-Control-Allow-Headers'] = '*'
            header['Access-Control-Allow-Credentials'] = True
            return response

    return app