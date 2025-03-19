
def check():
    print(f"The wallet has {money} bahts.") 
    
def deposit(amount):
    global money
    money += amount
    
def withdraw(amount):
    global money
    money -= amount

money = 1000
check()
#The wallet has 1000 bahts.
deposit(500)
check()
#The wallet has 1500 bahts.
withdraw(1000)
check()
#The wallet has 500 bahts.
