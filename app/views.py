from django.shortcuts import render
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def category(request):
    categories = Category.objects.all()
    ser = CategorySerializer(categories, many = True)
    return Response(ser.data)

@api_view(["GET"])
def cake_view(request):
    categories = Cake.objects.all()
    ser = CakeSerializer(categories, many = True)
    return Response(ser.data)