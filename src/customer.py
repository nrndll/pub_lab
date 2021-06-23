class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkeness = 0
        

    def reduce_wallet(self, amount):
        self.wallet -= amount

    def buy_drink(self, drink, pub):
        if pub.refuse_service(self):
            return "No!"
        if self.check_age():
            self.reduce_wallet(drink.price)
            pub.increase_till(drink.price)
            self.drunkeness += drink.alcohol_level

    def check_age(self):
        if self.age >= 18:
            return True
        return False

    def buy_food(self, food, pub):
        self.reduce_wallet(food.price)
        pub.increase_till(food.price)
        self.drunkeness -= food.rejuvenation_level