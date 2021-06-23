import unittest
from src.food import *

class TestFood(unittest.TestCase):

    def setUp(self):
        self.food = Food("Pakora", 5, 20)

    def test_food_has_name(self):
        self.assertEqual("Pakora", self.food.name)

    def test_food_has_price(self):
        self.assertEqual(5, self.food.price)

    def test_food_has_rejuvenation_level(self):
        self.assertEqual(20, self.food.rejuvenation_level)