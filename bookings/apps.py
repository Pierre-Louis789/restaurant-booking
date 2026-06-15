from django.apps import AppConfig


class BookingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookings'

    def ready(self):
        from bookings.models import Restaurant
        from datetime import time

        if Restaurant.objects.count() == 0:
            Restaurant.objects.create(
                name="Bistro West",
                description="A cosy modern bistro offering seasonal dishes.",
                address="14 West Street, Penzance",
                opening_time=time(11, 0),
                closing_time=time(22, 0),
                cuisine="Modern European",
                static_image="restaurant_images/bistro-west.jpg"
            )

            Restaurant.objects.create(
                name="Sakura Sushi House",
                description="Fresh sushi, sashimi, ramen, and Japanese dishes.",
                address="7 Cherry Blossom Lane, Penzance",
                opening_time=time(12, 0),
                closing_time=time(22, 30),
                cuisine="Japanese",
                static_image="restaurant_images/sakura.jpg"
            )

            print("🔥 Restaurants seeded on startup")
