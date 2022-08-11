from flask_login import LoginManager
from wtforms import SubmitField, TextAreaField, StringField, validators, ValidationError
from flask_wtf import FlaskForm

class ContactForm(FlaskForm):
    "Create Form for e-mail contact"

    name = StringField("Name", [validators.data_required()])
    email = StringField("Email", [validators.data_required(), validators.Email()])
    subject = StringField("Subject", [validators.data_required()])
    message = TextAreaField("Message", [validators.data_required()])
    submit = SubmitField("Send")