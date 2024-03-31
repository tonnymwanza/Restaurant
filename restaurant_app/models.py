from django.db import models
from . managers import FoodManager
# Create your models here.

class RestaurantTable(models.Model):
    person_name = models.CharField(max_length=50)
    email = models.EmailField(help_text='enter your email')
    phone_number = models.IntegerField()
    date_to_come = models.DateField(null=True, blank=True)
    time_to_come = models.DateTimeField(null=True, blank=True)
    number_of_people = models.IntegerField()
    message = models.TextField(null=True, blank=True)


class Food(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    food_manager = FoodManager() #the object manager for this class

    def __str__(self):
        return self.name

class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.food.name
    