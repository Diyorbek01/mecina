from django.contrib.auth.models import User
from django.db import models
from helper.models import BaseModel
from product.models import Product


# Create your models here.
class Wishlist(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_wishlist')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title


class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_cart')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_cart')
    amount = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.title} | {self.amount}"

    @property
    def subtotal(self):
        return self.amount * self.product.price


class Order(BaseModel):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Preaparing', 'Preaparing'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_summa = models.FloatField()
    number_of_products = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS, default='New')

    def __str__(self):
        return f"{self.total_summa}"



class OrderProduct(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()  # quantity of products
    price = models.FloatField()  # product price
    amount = models.FloatField()  # total amount of product price

    def __str__(self):
        return f"{self.product.title} | {self.amount}"
