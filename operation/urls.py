from django.urls import path
from .views import *

urlpatterns = [
    path('cart/', cart, name="cart"),
    path('insert/', insert, name="insert"),
    path('create_order/', create_order, name="create_order"),
    path('delete/<int:id>', delete, name="delete"),
    path('wishlist/', wishlist, name="wishlist"),
    path('delete-wishlist/<int:id>', delete_wishlist, name="delete-wishlist"),
]
