from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'hefirgbdgfnvirngiajerfibirnb'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///docspace_db.db'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User, Workspace

    create_database(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

def create_database(app):
    if not path.exists('docspace/docspace_db.db'):
        db.create_all(app=app)
        print('Database Created!')