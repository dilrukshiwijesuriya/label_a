# Generated by Django 4.0.3 on 2024-01-18 18:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_rename_delivery_cart_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='delivery',
            field=models.DateTimeField(auto_now=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
