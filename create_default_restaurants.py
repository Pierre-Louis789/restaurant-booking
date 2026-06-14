from bookings.models import Restaurant
from datetime import time

# Only create demo restaurants if none exist
if Restaurant.objects.count() == 0:

    Restaurant.objects.create(
        name="Bistro West",
        description="A cosy modern bistro offering seasonal dishes, local produce, and a relaxed dining atmosphere.",
        address="14 West Street, Penzance",
        opening_time=time(11, 0),
        closing_time=time(22, 0),
        cuisine="Modern European",
        static_image="restaurant_images/bistro-west.jpg"
    )

    Restaurant.objects.create(
        name="Sakura Sushi House",
        description="Fresh sushi, sashimi, ramen, and Japanese small plates served in a contemporary setting.",
        address="7 Cherry Blossom Lane, Penzance",
        opening_time=time(12, 0),
        closing_time=time(22, 30),
        cuisine="Japanese",
        static_image="restaurant_images/sakura.jpg"
    )

    Restaurant.objects.create(
        name="The Orangerie",
        description="Elegant dining with Mediterranean flavours, citrus-inspired dishes, and a bright botanical interior.",
        address="22 Garden Court, Penzance",
        opening_time=time(10, 0),
        closing_time=time(21, 30),
        cuisine="Mediterranean",
        static_image="restaurant_images/the-orangerie.jpg"
    )

    Restaurant.objects.create(
        name="The Weejus",
        description="A vibrant gastropub serving hearty comfort food, craft beers, and weekend live music.",
        address="3 Harbour Lane, Penzance",
        opening_time=time(11, 30),
        closing_time=time(23, 0),
        cuisine="Gastropub",
        static_image="restaurant_images/the-weejus.jpg"
    )

    print("Demo restaurants created.")

else:
    print("Restaurants already exist.")
