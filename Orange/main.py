from basket import Basket
from orange import Orange
from customer import Customer

basket = Basket("Kalasin")
orange1 = Orange(0.5, "Me", "2022-10-9")
orange2 = Orange(0.4, "De", "2022-10-11")
orange3 = Orange(0.3, "Ge", "2022-10-8")
customer1 = Customer("Au")
customer2 = Customer("We")

orange3.squeeze()

orange1.pick(basket)
orange2.pick(basket)
orange3.pick(basket)    

basket.sell(customer1)
basket.sell(customer2)

customer1.get_purchase_history()
customer2.get_purchase_history()

print("End Program")