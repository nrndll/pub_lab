class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []
        
        # {
        #     "beer" : 10,
        #     "absinth" : 30,
        #     "whiskey" : 20
        # }

    def increase_till(self, amount):
        self.till += amount

    # def find_drink_by_name(self, name):
    #     for drink in self.drinks:
    #         if drink == name:
    #             return drink