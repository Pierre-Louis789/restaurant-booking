from django.contrib.auth import get_user_model
from django.db.utils import OperationalError

User = get_user_model()

try:
    if not User.objects.filter(username="pierre").exists():
        User.objects.create_superuser(
            username="pierre",
            email="pierre@example.com",
            password="YourPassword123"
        )
        print("Superuser created.")
    else:
        print("Superuser already exists.")
except OperationalError:
    print("Database not ready.")