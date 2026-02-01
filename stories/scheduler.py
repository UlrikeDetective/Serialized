from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
# from stories.management.commands.email_backup import Command # TODO: Implement backup command

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    
    # Run every Sunday at midnight
    # scheduler.add_job(
    #     Command().handle, 
    #     'cron', 
    #     day_of_week='sun', 
    #     hour=0, 
    #     minute=0, 
    #     id="weekly_backup", 
    #     replace_existing=True
    # )
    print("Scheduler started (Jobs paused until backup command is implemented)")
    scheduler.start()
