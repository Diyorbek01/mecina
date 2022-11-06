from ckeditor.fields import RichTextField
from django.db import models

from helper.models import BaseModel


# Create your models here.
class Contact(BaseModel):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    subject = models.CharField(max_length=70, null=True, blank=True)
    text = models.TextField()

    def __str__(self):
        if self.subject:
            return self.subject
        return self.name


class Subscription(BaseModel):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Blog(BaseModel):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")
    description = RichTextField()

    def __str__(self):
        return self.title


class Setting(BaseModel):
    name = models.CharField(max_length=40, verbose_name="Name")
    facebook = models.CharField(max_length=40, verbose_name="Facebook")
    twitter = models.CharField(max_length=40, verbose_name="Twitter")
    youtube = models.CharField(max_length=40, verbose_name="Youtube")
    instagram = models.CharField(max_length=40, verbose_name="Instagram")
    logo = models.ImageField(upload_to="logo/", verbose_name="Logo")
    location = models.CharField(max_length=300, verbose_name="Location")
    phone_number = models.CharField(max_length=20, verbose_name="Phone Number")
    email = models.CharField(max_length=20, verbose_name="Email")
    title = models.CharField(max_length=300, verbose_name="Title")
    address = models.CharField(max_length=300, verbose_name="Address")
    working_days = models.CharField(max_length=100, verbose_name="Working days")
    working_hours = models.CharField(max_length=100, verbose_name="Working hours")
    off_days = models.CharField(max_length=100, verbose_name="Off days")
    off_hours = models.CharField(max_length=100, verbose_name="Off hours")
    about_us = RichTextField(verbose_name="About Us")
    about_us_image = models.ImageField(upload_to="images/", verbose_name="About Us Image")

    def __str__(self):
        return self.phone_number
