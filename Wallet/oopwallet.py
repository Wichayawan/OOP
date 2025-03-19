class Wallet:
    
    def __init__(self, name, money):
        self.name = name
        self.money = money 

    def check(self):
        print(f"The {self.name}'s wallet has {self.money} bahts.")

    def deposit(self, amount):
        self.money += amount

    def witdraw(self, amount):
        self.money -= amount
    

wallet1 = Wallet("Aheye" ,1000)
wallet2 = Wallet("Wichaya" ,2000)

wallet1.check()
#The wallet has 1000 bahts.
wallet2.check()
#The wallet has 2000 bahts.

print(f"{wallet1.name}'s wallet deposited 500 bahts.")
wallet1.deposit(500)
wallet1.check()
print(f"{wallet1.name}'s wallet withdrawed 1000 bahts.")
wallet2.witdraw(1000)
wallet2.check()