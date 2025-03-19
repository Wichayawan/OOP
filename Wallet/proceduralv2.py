def create(name, amount):
    return {"money": amount, "name": name}

def cheak(wallet):
    print(f"The {wallet['name']}'s wallet has {wallet['money']} bahts.")
    
def deposit(wallet, amount):
    wallet["money"] += amount
    
def witdraw(wallet, amount):
    wallet["money"] -= amount

wallet1 = create("Aheye", 1000)
wallet2 = create("Wichaya", 2000)
cheak(wallet1)
#The wallet has 1000 bahts.
cheak(wallet2)
#The wallet has 2000 bahts.
print(f"{wallet1['name']}'s wallet deposit 500 bahts.")
deposit(wallet1, 500)
cheak(wallet1)
#The wallet has 1500 bahts.
print(f"{wallet2['name']}'s wallet witdraw 1000 bahts.")
witdraw(wallet2, 1000)
cheak(wallet2)
#The wallet has 1000 bahts.



# active voice (V1)
# Wichayawan deposit wallet 