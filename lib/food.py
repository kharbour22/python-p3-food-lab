
class Food:
    all = []

    def __init__(self, name, price):
        self.name = name
        self.price = price
        
        Food.all.append(self)


    @classmethod
    def food_names(cls):
        return [food.name for food in cls.all]

    @classmethod
    def average_price(cls):
        list_of_prices = [food.price for food in cls.all]
        return (sum(list_of_prices)/len(list_of_prices))
    
    @classmethod
    def most_expensive(cls):
        return (max(cls.all, key=lambda food: food.price))


    