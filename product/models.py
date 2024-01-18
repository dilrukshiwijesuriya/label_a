from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} : {self.price}"

class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    completed = models.BooleanField(default=False)
    delivery = models.DateTimeField(blank=True, null=True)

    @property
    def sum_amount(self):
        return sum([item.price for item in self.items.all()])
