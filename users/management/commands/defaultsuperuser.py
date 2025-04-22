from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from decouple import config


class Command(BaseCommand):
    help = "Creates a superuser with the provided credentials"

    def handle(self, *args, **options):
        User = get_user_model()
        username = config("SUPERUSER_USERNAME", default="admin1")
        email = config("SUPERUSER_EMAIL", default="admin@example.com")
        password = config("SUPERUSER_PASSWORD", default="admin123")

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' created"))
        else:
            self.stdout.write(
                self.style.WARNING(f"Superuser '{username}' already exists")
            )
