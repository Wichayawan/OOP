class T:
    def f(self):
        print("Top")
        
class L(T):
    def f(self):
        print("Left")
        
class R(T):
    def f(self):
        print("Right")
        
class B(L, R):
    pass

b = B()
b.f()
print(B.mro())