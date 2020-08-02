from django.contrib import admin

# Register your models here.

# TODO If I want to see this models in database I need to register them

from .models import Product

admin.site.register(Product)
