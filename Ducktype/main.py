class Duck:
    def fly(self):
        print("Duck flying")

class Airplane:
    def fly(self):
        print("Airplane flying")

class Whale:
    def swim(self):
        print("Whale swimming")

def lift_off(entity):
    if hasattr(entity, 'fly'):
        entity.fly()
    else:
        print(f"{entity.__class__.__name__} can't fly")

duck = Duck()
airplane = Airplane()
whale = Whale()

lift_off(duck)
lift_off(airplane)
lift_off(whale)
