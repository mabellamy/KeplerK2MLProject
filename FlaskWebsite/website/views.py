from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/keplerdata')
def kepler_data():
    return render_template("keplerdata.html")

@views.route('/k2data')
def k2_data():
    return render_template("k2data.html")

@views.route('/models')
def models():
    return render_template("models.html")

@views.route('/results')
def results():
    return render_template("results.html")

@views.route('/process')
def process():
    return render_template("process.html")

@views.route('/sources')
def sources():
    return render_template("sources.html")

