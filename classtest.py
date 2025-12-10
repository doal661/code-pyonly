class MyClass:
    def __init__(self):
        self.data = []
    
    i = 12345

    def f(self):
        return 'hello world'

x = MyClass()
print(str(x.f()))

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

y = Complex(3.0, -4.5)
print(y.r+y.i)
