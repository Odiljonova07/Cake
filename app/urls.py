from django.urls import path
from .views import category, cake_view

urlpatterns = [
    path('category/', category),
    path('cakes/', cake_view)
]