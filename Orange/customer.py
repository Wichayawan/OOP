class Customer:
    
    def __init__(self, name):
        self.name = name
        self.history_purchase = ''
        
    def purchase(self, orange):
        self.history_purchase += f"{orange} \n"
        
    def get_purchase_history(self):
        print(f"{self.name}'s has history:\n {self.history_purchase}")