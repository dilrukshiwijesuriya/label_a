# Generated by Django 4.0.3 on 2024-01-18 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_cart_delivery_cart_completed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='Delivery',
            new_name='delivery',
        ),
    ]