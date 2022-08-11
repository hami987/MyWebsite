from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask_mail import Message, Mail
from flask_login import LoginManager

db = SQLAlchemy()
app = Flask(__name__)

DB_NAME = "WebsiteUsers.db"

mail = Mail()

app.config["MAIL_SERVER"] = "smtp.web.de"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = 'johannes-hammacher@web.de'
app.config["MAIL_PASSWORD"] = 'weaponfreak'

mail.init_app(app)

def create_app():
    app.config['SESSION_TYPE'] = 'memcached'
    app.config['SECRET_KEY'] = 'super secret key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    db.init_app(app)

    create_database(app)

    from website.views import views
    from website.auth import auth
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all(app=app)
            print('Created Database!')