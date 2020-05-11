from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_simplemde import SimpleMDE


db = SQLAlchemy()
photos = UploadSet('photos',IMAGES)
bcrypt = Bcrypt()
bootstrap = Bootstrap()
simple = SimpleMDE()


login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'
login_manager.session_protection = 'strong'


def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config_options[config_name])

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/authenticate')

    db.init_app(app)
    configure_uploads(app,photos)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)
    simple.init_app(app)


    return app
