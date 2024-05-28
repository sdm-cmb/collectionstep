from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from views import *

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)
