# Diamond Shape Problem in Multiple inheritance
class A:
    def med(self):
        print("This is a method from class A")
class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass
a=A() # This is a parent class
b=B() # this is a child class of A
c=C() # this is a child class of A
d=D() # this is a child class of B and 
d.med() # This will call the method from class A due to method resolution order (MRO)
print(D.__mro__) # This will display the method resolution order