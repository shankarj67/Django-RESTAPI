from django.urls import include, path
from .views import (
    RestaurantApiDetail, 
    RestaurantApiList, 
    RestaurantWiseSalesAPI,
    FoodAvailabilityAPI,
    Dump,
    TrendingFoodAPI,
    
    )


urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('users/', include('users.urls')),
    path("restaurant/<str:slug>/", RestaurantApiDetail.as_view(), name="detailview"),
    path("restaurant", RestaurantApiList.as_view(), name="listview"),
    path('totalsales/', RestaurantWiseSalesAPI.as_view(), name="salesview"),
    path('foodavailable/', FoodAvailabilityAPI.as_view(), name="foodview"),
    path('dump/', Dump.as_view(), name="dumpcsv"),
    path('trendingfood/', TrendingFoodAPI.as_view(), name="trendingfood" )
    

    
    
]
