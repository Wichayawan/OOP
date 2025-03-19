class Contract: 
    all_contracts = []
    
    def __init__(self, name, email):
        self.name = name #self.name คือการเรียกใช้ตัวแปรของตัวเรา
        self.email = email
        self.all_contracts.append(self)
        
    def __str__(self):
        return f"Contract -- name: {self.name},\n\t-- email: {self.email}"