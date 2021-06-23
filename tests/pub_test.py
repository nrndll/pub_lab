import unittest
from src.pub import *

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("Stonefire Tavern", 100)

    def test_pub_has_name(self):
        self.assertEqual("Stonefire Tavern", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100, self.pub.till)

    def test_pub_increase_till(self):
        self.pub.increase_till(10)
        self.assertEqual(110, self.pub.till)

