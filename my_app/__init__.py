__author__ = 'welserjr'

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.secret_key = 'some_random_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///catalog.db'
app.config['UPLOAD_FOLDER'] = os.path.realpath('.') + '/my_app/static/uploads'
db = SQLAlchemy(app)


from my_app.catalog.views import catalog
app.register_blueprint(catalog)

db.create_all()
