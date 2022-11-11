from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name="products"),
    path('details/<int:id>', details, name="products-details"),
    path('<int:id>', filter_product, name="products"),
    path('review/', review, name="review"),
]
