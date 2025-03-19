# Override with call super class 
# Problem is มี Top สองที

class T:
    def f(self):
        print("Top")
        
class L(T):
    def f(self):
        print("Left")
        super().f()
        
class R(T):
    def f(self):
        print("Right")
        super().f()
        
class B(L, R):
    def f(self):
        print("Bottom")
        super().f()
        

b = B()
b.f()
print(B.mro())