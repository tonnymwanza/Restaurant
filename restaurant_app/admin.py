from django.contrib import admin
from . models import RestaurantTable
from . models import Food
from . models import Order
# Register your models here.

@admin.register(RestaurantTable)
class AdminRestaurantTable(admin.ModelAdmin):
    list_display = [
        'person_name',
        'email',
        'phone_number',
        'date_to_come',
        'time_to_come',
        'number_of_people',
        'message'
    ]

@admin.register(Food)
class AdminFood(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'price',
        'image'
    ]

admin.site.register(Order)