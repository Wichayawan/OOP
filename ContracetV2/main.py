from contract import Contract   

c1 = Contract("John-A", "bob@ksu.ac.th", "123-456-7890")
c2 = Contract("Robert-B", "alice@ksu.ac.th" ,"459-632-0517")
c3 = Contract("Robert-John", "robertJohnbob@ksu.ac.th" ,"123-456-7890")
c4 = Contract("John-Robert", "johnRobert@ksu.ac.th" ,"521-364-7890")
c5 = Contract("Bob", "bob@ksu.ac.th", "123-065-4982")
c6 = Contract("Wichaya wavaAlice", "alice@ksu.ac.th", "066-419-5772")
c7 = Contract("Robert-John", "robertJohnbob@ksu.ac.th" ,"064-329-6518")
c8 = Contract("John-Robert", "johnRobert@ksu.ac.th" ,"123-456-7890")
c9 = Contract("Emily Aliceaa", "alice@ksu.ac.th", "985-216-3470")
c10 = Contract("Alice", "alice@ksu.ac.th", "982-541-3470")


print("All contracts")
for c in Contract.all_contracts:
    print(c)    
    
print()
print("All contracts with phone number")
for c in Contract.all_contracts.search("123-456-"):
    print(c)