import unittest
from src.pub import *
from src.customer import *
from src.drink import *

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("Stonefire Tavern", 100)
        self.customer = Customer("Jakub", 1000, 30)
        self.drink = Drink("Absinth", 30, 80)

    def test_pub_has_name(self):
        self.assertEqual("Stonefire Tavern", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100, self.pub.till)

    def test_pub_has_drinks(self):
        self.assertEqual(0, len(self.pub.drinks))

    def test_pub_can_add_drinks(self):
        self.pub.add_drink(self.drink)
        self.assertEqual(1, len(self.pub.drinks))

    def test_pub_increase_till(self):
        self.pub.increase_till(10)
        self.assertEqual(110, self.pub.till)

    def test_refuse_service_no(self):
        self.assertEqual(False, self.pub.refuse_service(self.customer))
    
    def test_refuse_service_yes(self):
        self.customer.drunkeness = 200
        self.assertEqual(True, self.pub.refuse_service(self.customer))