from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        Listing.objects.all().delete()
        locations = ['Nairobi', 'Mombasa', 'Kisumu', 'Naivasha']

        for i in range(10):
            Listing.objects.create(
                title=f"Listing {i+1}",
                description="This is a sample description.",
                price_per_night=random.uniform(50, 200),
                location=random.choice(locations),
                is_available=random.choice([True, False])
            )
        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
