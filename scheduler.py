from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from your_app.management.commands.email_backup import Command # Import your backup logic

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    
    # Run every Sunday at midnight
    scheduler.add_job(
        Command().handle, 
        'cron', 
        day_of_week='sun', 
        hour=0, 
        minute=0, 
        id="weekly_backup", 
        replace_existing=True
    )
    scheduler.start()