# constructors
#used for instantiating an object

class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0): #constructor
        
        #body of the constructor

        #assertion 
        assert price >= 0, f"Price {price} is not greater than or equal to 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to 0"
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity\
        
        # Actions to execute
        Item.all.append(self)
        


    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        # self.price = self.price * Item.pay_rate  
        self.price = self.price * self.pay_rate  
# item1 = Item("Apple", 100, 5)
# item2 = Item("Orange", 80, 2)

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())

# item1.apply_discount() #uses class attribute
# print(item1.price)

# item2.pay_rate = 0.7
# item2.apply_discount() #uses instance attribute
# print(item2.price)

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 18, 5)
item4 = Item("Mouse", 58, 5)
item5 = Item("Keyboard", 75, 5)

