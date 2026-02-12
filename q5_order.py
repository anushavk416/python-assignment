class Order:
    application = "amazon"
    ordersite = "hyderabad"
    taxpercent = 5    
    
    def __init__(self, orderid, price):
        self.orderid = orderid
        self.price = price
        self.placed = False

    def place_order(self):
        self.placed = True

    def cancel_order(self):
        if self.placed:
            self.placed = False
        else:
            print("Order not placed yet.")

    def calculate_total_price(self):
        tax = self.price * Order.taxpercent/100
        return self.price + tax

    @classmethod
    def update_taxpercent(cls, new_tax):
        cls.taxpercent = new_tax
        
        
o1 = Order(123, 2000)
o1.place_order()
print("Total Price:", o1.calculate_total_price())

Order.update_taxpercent(10)
print("Updated Total Price:", o1.calculate_total_price())

o1.cancel_order()
print("Order Placed:", o1.placed)

