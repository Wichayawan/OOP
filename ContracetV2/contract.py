from contrace_list import ContraceList

class Contract:
    all_contracts = ContraceList()
    
    def __init__(self, name, email, phone): 
        self.name = name
        self.email = email
        self.phone = phone
        self.all_contracts.append(self)
        
    def __str__(self):
        return f"Contract -- name: {self.name},\n\t-- email: {self.email},\n\t-- phone: {self.phone}"