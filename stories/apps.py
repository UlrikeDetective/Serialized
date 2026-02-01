from django.apps import AppConfig

class StoriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stories'

    def ready(self):
        # This ensures the scheduler starts once the app is ready
        # Avoid starting scheduler during migrations or static collection
        import sys
        if 'manage.py' in sys.argv and any(cmd in sys.argv for cmd in ['migrate', 'collectstatic', 'makemigrations']):
            return
            
        from . import scheduler
        try:
            scheduler.start()
        except Exception as e:
            print(f"Failed to start scheduler: {e}")