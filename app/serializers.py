from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        depth = 1
        fields = ['id', 'name', 'image', 'countProducts']


class CakeSerializer(serializers.ModelSerializer):
    discounted_price = serializers.SerializerMethodField() 
    # category = CategorySerializer(read_only=True)
    class Meta:
        model = Cake
        depth = 1
        fields = ['name', 'category', 'description', 
                  'price', 'isDiscount', 'info_number', 
                  'image', 'discounted_price'] 

    def get_discounted_price(self, obj): 
        return obj.discounted_price() if obj.discounted_price() is not None else None 

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if 'discounted_price' in data and data['discounted_price'] is None:
            data.pop('discounted_price')
        return data
        
