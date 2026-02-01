import os
import subprocess
from datetime import datetime
from django.core.management.base import BaseCommand
from django.core.mail import EmailMessage
from django.conf import settings

class Command(BaseCommand):
    help = 'Dumps the database and emails it to the admin'

    def handle(self, *args, **options):
        now = datetime.now().strftime("%Y-%m-%d")
        filename = f"backup-{now}.sql"
        # 1. Generate the dump using pg_dump
        # We use the DATABASE_URL from environment variables
        db_url = os.environ.get('DATABASE_URL')
        subprocess.run(f'pg_dump "{db_url}" > {filename}', shell=True)

        # 2. Prepare the email
        email = EmailMessage(
            subject=f"Weekly Database Backup: {now}",
            body="Attached is the weekly SQL dump of your hobby project.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.ADMIN_EMAIL],
        )
        
        # 3. Attach and Send
        with open(filename, 'rb') as f:
            email.attach(filename, f.read(), 'application/sql')
        
        email.send()
        
        # 4. Clean up the temporary file
        os.remove(filename)
        self.stdout.write(self.style.SUCCESS(f'Successfully sent {filename}'))