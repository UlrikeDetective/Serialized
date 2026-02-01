from django.apps import AppConfig

class StoriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stories'

    def ready(self):
        # This ensures the scheduler starts once the app is ready
        from . import scheduler
        scheduler.start()