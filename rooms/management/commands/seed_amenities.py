from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):

    help = "This command creates amenities"

    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         "--times",
    #         help="How many times  do you want me to tell you that I love you?",
    #     )

    def handle(self, *args, **options):
        amenities = [
            "Kitchen",
            "Shampoo",
            "Heating",
            "Air_conditioning",
            "Washer",
            "Dryer",
            "Wifi",
            "Breakfast",
            "Indoor_fireplace",
            "Hangers",
            "Iron",
            "Hair_dryer",
            "Laptop-friendly workspace",
            "TV",
            "Crib",
            "High_chair",
            "Self_check_in",
            "Smoke_alarm",
            "Carbon_monoxide_alarm",
            "Private bathroom",
            "Piano",
            "Beachfront",
            "Waterfront",
        ]

        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities create"))