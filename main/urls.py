from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('blog/', blog, name="blog"),
    path('blog-details/<int:id>', blog_details, name="blog-details"),
    path('contact/', contact, name="contact"),
    path('subscription/', subscription, name="subscription"),
    path('login/', login_register, name="login"),
    path('logout/', logout_func, name="logout"),
]
