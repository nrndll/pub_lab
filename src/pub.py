class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def increase_till(self, amount):
        self.till += amount

    def refuse_service(self, customer):
        if customer.drunkeness >= 100:
            return True
        else:
            return False
