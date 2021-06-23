import unittest
from src.customer import *
from src.pub import *
from src.drink import *

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Jakub", 1000, 30)
        self.pub = Pub("Star Bar", 0)
        self.drink = Drink("Absinth", 30, 80)
    
    def test_customer_has_name(self):
        self.assertEqual("Jakub", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(1000, self.customer.wallet)

    def test_customer_reduce_wallet(self):
        self.customer.reduce_wallet(10)
        self.assertEqual(990, self.customer.wallet)

    def test_customer_age(self):
        self.assertEqual(30, self.customer.age)

    def test_has_drunkeness_level(self):
        self.assertEqual(0, self.customer.drunkeness)

    def test_check_age_pass(self):
        expected = True
        actual = self.customer.check_age()
        self.assertEqual(True, actual)

    def test_check_age_fail(self):
        self.customer = Customer("Varg", 1, 12)
        self.assertEqual(False, self.customer.check_age())

    def test_buy_drink(self):
        self.customer.buy_drink(self.drink, self.pub)
        self.assertEqual(970, self.customer.wallet)
        self.assertEqual(30, self.pub.till)
        self.assertEqual(80, self.customer.drunkeness)

    def test_buy_drink_drunk_customer(self):
        self.customer.drunkeness = 360
        self.customer.buy_drink(self.drink, self.pub)
        self.assertEqual(1000, self.customer.wallet)
        self.assertEqual(0, self.pub.till)
        
    def test_buy_drink_customer_underage(self):
        self.customer.age = 13
        self.customer.buy_drink(self.drink, self.pub)
        self.assertEqual(1000, self.customer.wallet)
        self.assertEqual(0, self.pub.till)

