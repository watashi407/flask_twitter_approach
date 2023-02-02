from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from datetime import datetime, timedelta


db = SQLAlchemy()
DB_NAME = "database.db" 

client_id ="161481167666-bo6o274c7nge91vilidt36hncmmsuqna.apps.googleusercontent.com"
global_client ="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"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'watashi'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)
    db.init_app(app)


    from .views import views

    app.register_blueprint(views, url_prefix='/')

    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')