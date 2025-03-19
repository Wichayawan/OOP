from contract import Contract
from address import AddressHolder

class Friend(Contract, AddressHolder):
    def __init__(self, name, email, phone, street, province, city, code):
        Contract.__init__(self, name, email)
        AddressHolder.__init__(self, street, province, city, code)
        self.phone = phone

    def __str__(self):
        return Contract.__str__(self) + f", phone: {self.phone}\n" + AddressHolder.__str__(self)

if __name__ == "__main__":
    f1 = Friend("Bob", "bob@ksu.ac.th", "123-456-7890", "Karset Somboon", "Kalasin", "Kalasin", "46000")
    print(f1)