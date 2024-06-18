from django.db import models

from user.models import CustomUser

# Create your models here.
class Category(models.Model):
    id_category = models.AutoField(primary_key=True)
    name_category = models.CharField(max_length=32)

    def __str__(self):
        return self.name_category

class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    name_product = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)
    price_product = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_product = models.DecimalField(max_digits=10, decimal_places=2)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name_product}-{self.price_product}Fr - {self.quantity_product}Kg"
