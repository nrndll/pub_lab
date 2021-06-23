import unittest
from unittest.case import TestCase
from src.drink import *

class TestDrink(unittest.TestCase):
    
    def setUp(self):
        self.drink = Drink("Absinth", 30)

    def test_drink_has_name(self):
        self.assertEqual("Absinth", self.drink.name)

    def test_drink_has_price(self):
