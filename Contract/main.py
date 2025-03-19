from custom_contract import Friend, Supplier
from friend import Friend
from supplier import Supplier

f1 = Friend("Bob", "bob@ksu.ac.th", "123-456-7890")
f2 = Friend("Alice", "alice@ksu.ac.th", "987-654-3210")
f3 = f2
print(f1)
print(f2)
print("ID f1, f2, f3")
print(id(f1))
print(id(f2))
print(id(f3))   
print("ID all contracts")
print(id(f1.all_contracts))
print(id(f2.all_contracts))
print(id(Friend.all_contracts))
s = Supplier("Pizza Hut", "supplier@ksu.ac.th")
s.order("8 chicken Wings")
for p in s.all_contracts:
    print(p)