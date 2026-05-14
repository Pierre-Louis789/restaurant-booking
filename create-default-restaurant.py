from bookings.models import Restaurant


if Restaurant.objects.count() == 0:

    Restaurant.objects.create(
        name="Bistro West",
        description="A cosy modern bistro offering seasonal dishes, local produce, and a relaxed dining atmosphere.",
        cuisine="Modern European",
        address="14 West Street, Penzance",
        opening_time="11:00",
        closing_time="22:00",
        static_image="restaurant_images/bistro-west.jpg"
    )

    Restaurant.objects.create(
        name="Sakura Sushi House",
        description="Fresh sushi, sashimi, ramen, and Japanese small plates served in a contemporary setting.",
        cuisine="Japanese",
        address="7 Cherry Blossom Lane, Penzance",
        opening_time="12:00",
        closing_time="22:30",
        static_image="restaurant_images/sakura.jpg"
    )

    Restaurant.objects.create(
        name="The Orangerie",
        description="Elegant dining with Mediterranean flavours, citrus-inspired dishes, and a bright botanical interior.",
        cuisine="Mediterranean",
        address="22 Garden Court, Penzance",
        opening_time="10:00",
        closing_time="21:30",
        static_image="restaurant_images/the-orangerie.jpg"
    )

    Restaurant.objects.create(
        name="The Weejus",
        description="A vibrant gastropub serving hearty comfort food, craft beers, and weekend live music.",
        cuisine="Gastropub",
        address="3 Harbour Lane, Penzance",
        opening_time="11:30",
        closing_time="23:00",
        static_image="restaurant_images/the-weejus.jpg"
    )

    print("Demo restaurants created.")

else:
    print("Restaurants already exist.")