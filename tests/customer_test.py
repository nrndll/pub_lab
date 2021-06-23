import unittest
from src.customer import *

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Jakub", 1000)
    
    def tests_customer_has_name(self):
        self.assertEqual("Nathan", self.customer.name)

    