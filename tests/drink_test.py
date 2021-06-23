import unittest
from src.drink import *

class TestDrink(unittest.TestCase):
    
    def setUp(self):
        self.drink = Drink("Absinth", 30, 80)

    def test_drink_has_name(self):
        self.assertEqual("Absinth", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(30, self.drink.price)

    def test_drink_has_alcohol_level(self):
        self.assertEqual(80, self.drink.alcohol_level)