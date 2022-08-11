import ast
from website import db
from flask_login import UserMixin

class WebsiteUsers(db.Model, UserMixin):

    __tablename__ = "WebsiteUsers"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200))
    password = db.Column(db.String(200))
    date_joined = db.Column(db.String(200))
