import unittest
from src.customer import *
from src.pub import *
from src.drink import *

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Jakub", 1000)
        self.pub = Pub("Star Bar", 0)
        self.drink = Drink("Absinth", 30)
    
    def tests_customer_has_name(self):
        self.assertEqual("Jakub", self.customer.name)

    def tests_customer_reduce_wallet(self):
        self.customer.reduce_wallet(10)
        self.assertEqual(990, self.customer.wallet)

    def tests_buy_drink(self):
        # drink = Drink("Absinth", 30)
        # drink = self.drink
        # pub = self.pub
        self.customer.reduce_wallet(self.drink.price)
        self.pub.increase_till(self.drink.price)
        self.assertEqual(970, self.customer.wallet)
        self.assertEqual(30, self.pub.till)

        

