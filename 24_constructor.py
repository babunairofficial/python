# constructors
#used for instantiating an object

class Item:
    def __init__(self, name: str, price: float, quantity=0): #constructor
        
        #body of the constructor

        #assertion 
        assert price >= 0, f"Price {price} is not greater than or equal to 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to 0"
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity
    
item1 = Item("Apple", 100, 5)
item2 = Item("Orange", 80, 2)

print(item1.calculate_total_price())
print(item2.calculate_total_price())