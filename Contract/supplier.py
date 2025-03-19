from contract import Contract

class Supplier(Contract):
    def order(self, order):
        print(f"Send: {order} to {self.name}")