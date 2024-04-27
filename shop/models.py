from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from faker import Faker

class CustomUser(AbstractUser):
    USER_ROLES = (
        ('admin', 'Admin'),
        ('user', 'User'),
        ('guest', 'Guest'),
    )
    role = models.CharField(max_length=10, choices=USER_ROLES, default='guest')
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.email  # You might want to adjust this based on your requirements


class Cart(models.Model):
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE, related_name='carts')
    quantity = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return f'{self.product}, {self.quantity}, {self.created_date}'


class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    address = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email  # You might want to adjust this based on your requirements


class LineItem(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE)
    cart = models.ForeignKey('shop.Cart', on_delete=models.CASCADE)
    order = models.ForeignKey('shop.Order', on_delete=models.CASCADE, default='')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity}, {self.product}, {self.cart}, {self.created_date}'

    @classmethod
    def get_order_items(cls, order_id):
        return cls.objects.filter(order_id=order_id)


class Order(models.Model):
    customer = models.ForeignKey('shop.Customer', on_delete=models.CASCADE, default='Order')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order #{self.pk} for {self.customer}'


class Product(models.Model):
    BRAND_CHOICES = (
        ('Nike', 'Nike'),
        ('Adidas', 'Adidas'),
        ('Reebok', 'Reebok'),
        ('Converse', 'Converse'),
    )

    GENDER_CHOICES = (
        ('Men', 'Men'),
        ('Women', 'Women'),
    )

    TYPE_CHOICES = (
        ('Basketball', 'Basketball'),
        ('Running', 'Running'),
        ('Casual', 'Casual'),
    )

    brand = models.CharField(max_length=20, choices=BRAND_CHOICES, default='Nike')
    model = models.CharField(max_length=100, default='')
    product_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='Casual')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Men')
    size = models.CharField(max_length=10, default='')
    color = models.CharField(max_length=20, default='')
    material = models.CharField(max_length=20, default='')
    name = models.CharField(max_length=200, default='')
    price = models.DecimalField(decimal_places=2, max_digits=10)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.model}"