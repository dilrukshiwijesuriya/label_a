from django.contrib import admin
from product import models

@admin.register(models.Item)
class AdminItem(admin.ModelAdmin):
    list_display = ("name", "price",)

admin.site.register(models.Cart)
