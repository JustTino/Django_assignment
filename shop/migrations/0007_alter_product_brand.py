# Generated by Django 4.1.2 on 2024-04-27 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_rename_cartaddress_cart_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(choices=[('Nike', 'Nike'), ('Adidas', 'Adidas'), ('Reebok', 'Reebok'), ('Converse', 'Converse')], default='Nkie', max_length=20),
        ),
    ]