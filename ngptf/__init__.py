from flask import Flask
from flask.ext import restful

from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
api_rest = restful.Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

import ngptf.api

@app.route('/')
def main():
    return app.send_static_file('index.html')