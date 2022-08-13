import os.path
import json
from flask import jsonify,Blueprint, render_template, request,\
    flash, redirect, url_for, send_from_directory, Response, send_file,Markup, session
from flask_login import login_required, current_user
from website import db, mail
import plotly
from forms import ContactForm
from flask_mail import Message
from data_analysis import transportationDataVis

views = Blueprint('views', __name__)

@views.route("/", methods=["GET","POST"])
@views.route("/home", methods=["GET","POST"])
def home():
    return render_template("home.html")

@views.route("/education", methods=["GET","POST"])
def education():
    return render_template("edu.html")

@views.route("/projects", methods=["GET","POST"])
def projects():
    return render_template("projects.html")

@views.route("/contact", methods=["GET","POST"])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        form.name = request.form['Name']
        form.subject = request.form['Subject']
        form.email = request.form['Email']
        form.message = request.form["Message"]

        if form.name != "" and form.subject != "" and form.email != "" and form.message != "":
            msg = Message(form.subject, sender="johannes-hammacher@web.de",
                          recipients=['johannes-hammacher@web.de'])
            msg.body = """
                              From: %s <%s>
                              %s
                              """ % (form.name, form.email, form.message)
            mail.send(msg)
            flash("Message sent successfully", category="success")
            return redirect(url_for("views.home"))
        else:
            flash('All fields are required.', category="error")
            return render_template('contact.html', form=form)
    elif request.method == 'GET':
        return render_template('contact.html', form=form)

@views.route("/dashboard_python",methods=["GET"])
def dashboard_python():
    figures = transportationDataVis("website/datasets/tfl-journeys-type.csv")
    line_plt = json.dumps(figures[0], cls=plotly.utils.PlotlyJSONEncoder)
    pie_chart = json.dumps(figures[1], cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("Charts.html", line_plot=line_plt, pie_chart=pie_chart)



