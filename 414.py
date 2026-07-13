# Diamond Shape Problem in Multiple inheritance
# Answer--> The DSP is an ambiguity that arises in object-oriented programming when a class inherits from two classes that have a common base class. This can lead to confusion about which method or attribute to use from the base class.
class A:
    def met(self):
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
d=D() # this is a child class of B and C
d.met() # This will call the method from class A due to method resolution order (MRO)
print(D.__mro__) # This will display the method resolution order

#----------------------------------------------------------------->

class A:
    def met(self):
        print("This is a method from class A")
class B(A):
    def met(self):
        print("This is a method from class B")
class C(A):
    pass
class D(B, C):
    pass
d.met() # This will call the method from class B due to method resolution order (MRO)
print(D.__mro__) # This will display the method resolution order

#----------------------------------------------------------------->

class A:
    def met(self):
        print("This is a method from class A")
class B(A):
    def met(self):
        print("This is a method from class B")
class C(A):
    def met(self):
        print("This is a method from class C")
class D(B, C):
    pass
d.met() # This will call the method from class B due to method resolution order (MRO)
print(B.__mro__) # This will display the method resolution order

#----------------------------------------------------------------->

class A:
    def met(self):
        print("This is a method from class A")
class B(A):
    def met(self):
        print("This is a method from class B")
class C(A):
    def met(self):
        print("This is a method from class C")
class D(B, C): #class D(C,B): # This will change the method resolution order (MRO)
    def met(self):
        print("This is a method from class D")
d=D() # This will call the method from class D due to method resolution order (MRO)
d.met() # This will call the method from class D due to method resolution order (MRO)
print(D.__mro__) # This will display the method resolution order


# Kai sari languages me Diamond shape problem ka solution yehi hai ki aapko method resolution order (MRO) ka dhyan rakhna hoga. Python me MRO ko samajhne ke liye aap `__mro__` attribute ka use kar sakte hain jo ki class hierarchy ko dikhata hai.
# aur kyu lan me multiple inheritance support hi nhi krta hai....EXAMPLE- C,C++
