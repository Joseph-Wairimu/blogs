from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
bootstrap = Bootstrap()
def create_app(config_name):

    app = Flask(__name__)
    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)
   
    bootstrap.init_app(app)
    #register blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    return app