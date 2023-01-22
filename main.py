from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

current_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(current_dir, "database.sqlite3") 
db = SQLAlchemy()
db.init_app(app)

from model import *
db.init_app(app)
app.app_context().push()

@app.route('/')
def Hello_world():
    return render_template('index.html')

@app.route('/sign-in')
def sign_in():
    return render_template('sign-in.html')

@app.route('/sign-up')
def sign_up():
    return render_template('sign-up.html')

@app.route('/login-action')
def login_action():
    pass


if __name__ == '__main__':
    app.run(debug=True)