import unittest
from src.customer import *
from src.pub import *
from src.drink import *

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Jakub", 1000, 30)
        self.pub = Pub("Star Bar", 0)
        self.drink = Drink("Absinth", 30, 80)
    
    def tests_customer_has_name(self):
        self.assertEqual("Jakub", self.customer.name)

    def tests_customer_reduce_wallet(self):
        self.customer.reduce_wallet(10)
        self.assertEqual(990, self.customer.wallet)

    def tests_customer_age(self):
        self.assertEqual(30, self.customer.age)

    def test_has_drunkeness_level(self):
        self.assertEqual(0, self.customer.drunkeness)

    def tests_buy_drink(self):
        if self.customer.check_age():
            self.customer.buy_drink(self.drink, self.pub)
            self.assertEqual(970, self.customer.wallet)
            self.assertEqual(30, self.pub.till)
            self.assertEqual(80, self.customer.drunkeness)

        

