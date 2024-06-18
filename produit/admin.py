from django.contrib import admin

from produit.models import Category, Product

# Register your models here.
admin.site.register([Category, Product])