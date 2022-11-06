from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="products"),
    path('details/<int:id>', details, name="products-details"),
    path('<int:id>', filter_product, name="products"),
    path('review/', review, name="review"),
]
