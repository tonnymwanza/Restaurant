from django.test import TestCase

from .models import RestaurantTable
from . models import Food
from . models import Salad
from . models import Specialty
from . models import Starter
# Create your tests here.

class RestaurantTableTestCase(TestCase):

    def setUp(self):
        restaurant_table = RestaurantTable.objects.create(
            person_name='tinny', email='tonnimwanza@gmail.com', phone_number='079186734', number_of_people=7
        )

    def test_restaurant(self):
        restaurant_obj = RestaurantTable.objects.count()
        self.assertEqual(restaurant_obj, 1)


class FoodTestCase(TestCase):

    def setUp(self):
        food = Food.food_manager.create(
            name='pilau',description='fried rice',price=120,image='food.jpeg'
        )

    def test_food(self):
        food = Food.food_manager.filter(name__iexact='meat')
        self.assertFalse(food)

class SaladTestCase(TestCase):

    def setUp(self):
        salad = Salad.food_manager.create(
            name = 'onions', description='green onions', price=150, image='onion.jpeg'
        )

    def test_salad(self):
        salad = Salad.food_manager.count()
        self.assertEqual(salad, 1)

class SpecialtyTestCase(TestCase):

    def setUp(self):
        specialty = Specialty.food_manager.create(
            name='chicken', description='fried chicken', price=750, image='chicken.jpeg'
        )

    def test_specialty(self):
        specialty = Specialty.food_manager.filter(name__iexact='chicken')
        self.assertTrue(specialty)

class StarterTestCase(TestCase):

    def setUp(self):
        starter = Starter.food_manager.create(
            name='mango', description='yellow mangoes', price=79, image='mango.jpeg'
        )

    def test_starter(self):
        starter = Starter.food_manager.count()
        self.assertEqual(starter, 1)