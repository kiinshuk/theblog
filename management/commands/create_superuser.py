# your_app/management/commands/create_superuser.py
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = 'Creates a superuser from environment variables'

    def handle(self, *args, **options):
        User = get_user_model()
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
        
        if not password:
            self.stdout.write(
                self.style.ERROR('❌ DJANGO_SUPERUSER_PASSWORD not set')
            )
            return
        
        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING(f'⚠️ User {username} already exists')
            )
            return
        
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        self.stdout.write(
            self.style.SUCCESS(f'✅ Superuser {username} created successfully!')
        )