from django.db import models
from store.models import Product

# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=225, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='product')
    cart = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart')
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.product