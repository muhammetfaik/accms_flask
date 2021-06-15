from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime


app = Flask(__name__)

moment = Moment(app)

bootstrap  = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html',current_time=datetime.utcnow())

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404


@app.errorhandler(500)
def interval_server_error(e):
    return render_template('500.html'),500


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)