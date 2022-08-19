from flask import Flask
import numpy as np
import pandas as pd


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'live long and prosper'

    from .views import views

    app.register_blueprint(views, url_prefix = '/')

    return app