from django.contrib import admin
from .models import FoodDetail, OrderDetail
from import_export.admin import ImportExportActionModelAdmin


@admin.register(FoodDetail)
class StartupAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)} 

@admin.register(OrderDetail)
class StartupAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("restaurant_name",)} 
