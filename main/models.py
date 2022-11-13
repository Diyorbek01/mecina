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
    name = models.CharField(max_length=40, verbose_name="Name", null=True, blank=True)
    facebook = models.CharField(max_length=40, verbose_name="Facebook", null=True, blank=True)
    twitter = models.CharField(max_length=40, verbose_name="Twitter", null=True, blank=True)
    youtube = models.CharField(max_length=40, verbose_name="Youtube", null=True, blank=True)
    instagram = models.CharField(max_length=40, verbose_name="Instagram", null=True, blank=True)
    logo = models.ImageField(upload_to="logo/", verbose_name="Logo", null=True, blank=True)
    location = models.CharField(max_length=300, verbose_name="Location", null=True, blank=True)
    phone_number = models.CharField(max_length=20, verbose_name="Phone Number", null=True, blank=True)
    email = models.CharField(max_length=20, verbose_name="Email", null=True, blank=True)
    title = models.CharField(max_length=300, verbose_name="Title", null=True, blank=True)
    address = models.CharField(max_length=300, verbose_name="Address", null=True, blank=True)
    working_days = models.CharField(max_length=100, verbose_name="Working days", null=True, blank=True)
    working_hours = models.CharField(max_length=100, verbose_name="Working hours", null=True, blank=True)
    off_days = models.CharField(max_length=100, verbose_name="Off days", null=True, blank=True)
    off_hours = models.CharField(max_length=100, verbose_name="Off hours", null=True, blank=True)
    about_us = RichTextField(verbose_name="About Us", null=True, blank=True)
    about_us_image = models.ImageField(upload_to="images/", verbose_name="About Us Image", null=True, blank=True)

    def __str__(self):
        return self.phone_number
