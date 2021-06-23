import unittest
from src.pub import *

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("Stonefire Tavern", 100.00)

    def test_pub_has_name(self):
        self.assertEqual("Stonefire Tavern", self.pub.name)

    def test_pub_has_counter(self):
        self.assertEqual(100, self.pub.till)

