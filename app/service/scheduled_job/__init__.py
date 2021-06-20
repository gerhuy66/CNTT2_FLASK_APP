from app import app
from flask_jobs import JobScheduler
import datetime,time

jobs = JobScheduler(
    app,
    # SERVER_HOST_URL='https://mysite.com/', # only required for linux
    deleteOldJobs=False,# whether to keep old jobs in the database
)

def Callback():
    now = datetime.datetime.now()
    print('Scheduled Job: '+str(now))
    # get_link_linkedin.crawl_profile("automatic_crawl")

def create_repeat_job():
    dt = datetime.datetime.utcnow()
    jobs.RepeatJob(
    func=Callback,
    name='RepeatJob Job at {}'.format(time.asctime()),
    seconds=30, # can also pass "weeks", "days", "minutes", "hours"
)


# Schedule a job to repeat at the given interval

