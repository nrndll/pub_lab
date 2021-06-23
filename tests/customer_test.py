import unittest
from src.customer import *

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Jakub", 1000)
    
    def tests_customer_has_name(self):
        self.assertEqual("Jakub", self.customer.name)

    def tests_customer_reduce_wallet(self):
        self.customer.reduce_wallet(10)
        self.assertEqual(990, self.customer.wallet)