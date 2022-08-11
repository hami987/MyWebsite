import datetime
import requests
from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
import pandas as pd

auth = Blueprint('auth',__name__)

@auth.route("/login", methods=["GET","POST"])
def login():
    return render_template("home.html")


