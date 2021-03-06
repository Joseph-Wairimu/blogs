from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
from flask_simplemde import SimpleMDE
import os


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
bootstrap = Bootstrap()
mail = Mail()
simple = SimpleMDE()
photos = UploadSet('photos',IMAGES)
db = SQLAlchemy()
def create_app(config_name):

    app = Flask(__name__)
    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    bootstrap.init_app(app)
    db.init_app(app)
    with app.app_context():
       db.create_all()
    # configure UploadSet
    configure_uploads(app,photos)

    mail.init_app(app)
    simple.init_app(app)

  
    from .models import User
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    #register blueprint

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app