import flask
from flask import json, render_template, request, session, Response,jsonify,redirect,url_for,flash,make_response,Flask
from flask_jobs import JobScheduler
import datetime
import time




app = Flask(__name__,static_url_path='/static')
app.debug = True


from app.controller import main_controller
from app.database import mysql_db
from app.service.selenium import get_link_linkedin
mysql_db.create_all()


jobs = JobScheduler(
    app,
    # SERVER_HOST_URL='https://mysite.com/', # only required for linux
    deleteOldJobs=False,# whether to keep old jobs in the database
)

def Callback():
    now = datetime.datetime.now()
    print('Scheduled Job: '+str(now))
    get_link_linkedin.crawl_profile("automatic_crawl")


# Schedule a job to repeat at the given interval
with app.app_context():
    dt = datetime.datetime.utcnow()
    jobs.RepeatJob(
        func=Callback,
        name='RepeatJob Job at {}'.format(time.asctime()),
        seconds=30, # can also pass "weeks", "days", "minutes", "hours"
    )

@app.route('/delete/<ID>')
def Delete(ID):
    job = jobs.GetJob(int(ID))
    job.Delete()
    return redirect('/')

















@app.shell_context_processor
def make_shell_context():
    return dict(dg=mysql_db,jobs = jobs)