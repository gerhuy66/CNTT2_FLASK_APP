import flask
from flask import json, render_template, request, session, Response,jsonify,redirect,url_for,flash,make_response,Flask

import datetime
import time




app = Flask(__name__,static_url_path='/static')
app.debug = True


from app.controller import main_controller
# from app.database import mysql_db



# mysql_db.create_all()
















# @app.shell_context_processor
# def make_shell_context():
#     return dict(dg=mysql_db)