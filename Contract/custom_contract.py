from contract import Contract

class Friend(Contract):
    def __init__(self, name, email, phone): 
        print(id(super()))
        super().__init__(name, email)
        self.phone = phone
        
    def __str__(self):
        return f"{super().__str__()} phone: {self.phone}"

class Supplier(Contract):
    def order(self, order):
        print(f"Send: {order} to {self.name}")