from django.core.management.base import BaseCommand
from faker import Faker
import random
import decimal  # Add this line for the decimal module

from shop.models import Cart, Customer, LineItem, Order, Product, CustomUser

class Command(BaseCommand):
    help = 'Load data into the tables'

    def handle(self, *args, **options):

        # Drop the tables - use this order due to foreign keys - so that we can rerun the file as needed without repeating values
        Cart.objects.all().delete()
        LineItem.objects.all().delete()
        Order.objects.all().delete()
        Product.objects.all().delete()
        Customer.objects.all().delete()
        CustomUser.objects.all().delete()
        print("Tables dropped successfully")

        fake = Faker()

        # Create some customers
        for i in range(10):
            first_name = fake.first_name()
            last_name = fake.last_name()
            username = first_name + last_name
            user = CustomUser.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=fake.ascii_free_email(), 
                password='p@ssw0rd'
            )
            customer = Customer.objects.create(user=user)
            print(f"Created customer: {customer}")

        # Create some products
        for i in range(60):
            product = Product.objects.create(
                name=fake.catch_phrase(),
                price=decimal.Decimal(random.randrange(155, 899)) / 100,
            )
            print(f"Created product: {product}")

        # Create some carts 
        products = list(Product.objects.all())
        for i in range(10):
            random_id = random.randint(0, len(products) - 1)
            cart = Cart.objects.create(
                product=products[random_id],
                quantity=random.randrange(1, 42),
            )
            print(f"Created cart: {cart}")

        # Create orders from customers
        customers = Customer.objects.all()
        for customer in customers:  
            for i in range(3):
                order = Order.objects.create(
                    customer=customer,
                )
                print(f"Created order: {order}")
               
        # Attach line_items to orders
        orders = Order.objects.all()
        carts = Cart.objects.all()
        for order in orders:
            for cart in carts:
                line_item = LineItem.objects.create(
                    quantity=cart.quantity,
                    product=cart.product,
                    cart=cart,
                    order=order,
                )
                print(f"Created line item: {line_item}")

        print("Tables successfully loaded")
