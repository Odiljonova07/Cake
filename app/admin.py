from django.contrib import admin
from .models import Category, Cake

admin.site.register([Category, Cake])
