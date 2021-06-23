import unittest
from src.pub import *
from src.customer import *

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("Stonefire Tavern", 100)
        self.customer = Customer("Jakub", 1000, 30)

    def test_pub_has_name(self):
        self.assertEqual("Stonefire Tavern", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100, self.pub.till)

    def test_pub_increase_till(self):
        self.pub.increase_till(10)
        self.assertEqual(110, self.pub.till)

    def test_check_age(self):
        expected = True
        actual = self.customer.check_age()
        self.assertEqual(True, actual)

    def test_refuse_service(self):
        self.assertEqual(False, self.pub.refuse_service(self.customer))