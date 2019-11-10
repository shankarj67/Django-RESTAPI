from rest_framework import serializers
from restaurant import models


class FoodDetailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = models.FoodDetail
    

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = models.OrderDetail    