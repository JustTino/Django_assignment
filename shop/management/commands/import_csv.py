import csv
from decimal import Decimal, InvalidOperation
from django.core.management.base import BaseCommand
from shop.models import Product

class Command(BaseCommand):
    help = 'Import data from a CSV file to the Product model'

    def handle(self, *args, **kwargs):
        csv_file = 'data/data_file.csv'  
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f, delimiter=",")
            for row in reader:
                brand, model, product_type, gender, size, color, material, price = row
                # Convert price to Decimal with error handling
                try:
                    price = Decimal(price.replace('$', ''))
                except InvalidOperation:
                    # Log error or handle appropriately
                    print(f"Invalid price value: {price}")
                    continue
                Product.objects.create(
                    brand=brand,
                    model=model,
                    product_type=product_type,
                    gender=gender,
                    size=size,
                    color=color,
                    material=material,
                    price=price
                )
        self.stdout.write(self.style.SUCCESS('Data imported successfully!'))
