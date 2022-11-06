from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from django.db.models import Avg
from django.urls import reverse
from django.utils.safestring import mark_safe

from helper.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Create your models here.
class Product(BaseModel):
    title = models.CharField(max_length=200)
    description = RichTextField()
    price = models.BigIntegerField()
    amount = models.PositiveIntegerField()
    is_new = models.BooleanField(default=False)
    count_sold = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category', null=True)

    def __str__(self):
        return self.title

    @property
    def reviews(self):
        return Review.objects.filter(product_id=self.id)

    @property
    def rate(self):
        number = Review.objects.filter(product_id=self.id).aggregate(avarage=Avg("rate"))['avarage']
        return round(number, 1)
    @property
    def number_review(self):
        return Review.objects.filter(product_id=self.id).count()


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_image')
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.product.title


class Review(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField(default=0)
    comment = models.TextField()

    def __str__(self):
        return self.comment
