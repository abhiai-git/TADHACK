from flask import Flask
from flask.ext.login import LoginManager
from flask_sslify import SSLify


app = Flask(__name__)
sslify = SSLify(app)

app.config.from_object('config')
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

from app import views
