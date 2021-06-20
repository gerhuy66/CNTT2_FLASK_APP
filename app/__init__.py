import flask
from flask import json, render_template, request, session, Response,jsonify,redirect,url_for,flash,make_response,Flask
# from flask_jobs import JobScheduler
import datetime
import time
from flask_s3 import FlaskS3



app = Flask(__name__,static_url_path='/static')
app.config['FLASKS3_BUCKET_NAME'] = 'cvsearchwebstorage'
app.config['AWS_ACCESS_KEY_ID'] = 'AKIAXYZRVWASFJT4DGP7'
app.config['AWS_SECRET_ACCESS_KEY'] = '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'
s3 = FlaskS3(app)
app.static_url_path ='https://cvsearchwebstorage.s3.ap-southeast-1.amazonaws.com/'
app.debug = True


from app.controller import main_controller
from app.database import mysql_db
# from app.service.selenium import get_link_linkedin
mysql_db.create_all()

# from app.service import scheduled_job
# scheduled_job.create_repeat_job()



















@app.shell_context_processor
def make_shell_context():
    return dict(dg=mysql_db)