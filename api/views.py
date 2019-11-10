from restaurant import models
from .serializers import OrderDetailSerializer
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from rest_framework import generics
from api.services import APILogic
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.settings import api_settings
from rest_framework_csv.renderers import CSVRenderer
from datetime import date


class RestaurantApiDetail(RetrieveAPIView):
    queryset = models.OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
    lookup_field = "slug"


class RestaurantApiList(ListAPIView):
    queryset = models.OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer


class RestaurantWiseSalesAPI(ListAPIView):
    #queryset = models.OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['slug', 'order_timestamp'] 
    renderer_classes = [JSONRenderer] 

    def get_queryset(self):
        queryset = models.OrderDetail.objects.all()
        slug = self.request.query_params.get('slug')
        order_timestamp = self.request.query_params.get('order_timestamp')
        
        
        if order_timestamp:
            queryset = queryset.filter(slug=slug).filter(order_timestamp__date = order_timestamp)
        else:
            queryset = queryset.filter(slug=slug)

        return queryset

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = OrderDetailSerializer(queryset, many=True)
        result = APILogic.restaurant_wise_sales(queryset)
        return HttpResponse(result)   
        
class FoodAvailabilityAPI(ListAPIView):
    #queryset = models.OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['food', 'order_timestamp'] 
   

    def get_queryset(self):
        #queryset = models.OrderDetail.objects.all()
        food = self.request.query_params.get('food')
        order_timestamp = self.request.query_params.get('order_timestamp') 
        queryset = models.OrderDetail.objects.filter(order_timestamp__date = order_timestamp)
        return food, queryset

    def list(self, request):    
        # Note the use of `get_queryset()` instead of `self.queryset`
        food, queryset = self.get_queryset()
        serializer = OrderDetailSerializer(queryset, many=True)
        result = APILogic.food_availablility(food, queryset)
        return HttpResponse(result)   
              

class Dump(ListAPIView):
    #queryset = models.OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['slug', 'order_timestamp'] 
    renderer_classes = [CSVRenderer]
   

    def get_queryset(self):
        #queryset = models.OrderDetail.objects.all()
        slug = self.request.query_params.get('slug')
        order_timestamp = self.request.query_params.get('order_timestamp') 
        print(order_timestamp)
        queryset = models.OrderDetail.objects.filter(slug=slug)
        return queryset
  
    def list(self, request):    
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = OrderDetailSerializer(queryset, many=True)
        return Response(serializer.data) 

class TrendingFoodAPI(ListAPIView):
    #queryset = models.OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['slug', 'order_timestamp'] 
    renderer_classes = [JSONRenderer] 

    def get_queryset(self):
        queryset = models.OrderDetail.objects.all()
        slug = self.request.query_params.get('slug')
        order_timestamp = self.request.query_params.get('order_timestamp')
        queryset = queryset.filter(slug=slug)
        return queryset

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = OrderDetailSerializer(queryset, many=True)
        result = APILogic.trending_items(queryset)
        print(type(result))
        return HttpResponse(result)  