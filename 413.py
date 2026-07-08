 # Super() and Overriding
class A:
    class_var = " I am a Class Variable in Class A"
    def __init__(self):
        self.instance_var = " I am an Instance Variable in Class A"
        self.var = "I am inside class A's Constructor" #here , this is an instance variable, not a class variable.
        self.class_var = "Instance var in Class A"
class B(A):
    class_var2 = " I am a Class Variable in Class B"
a=A()
b=B()
print(a.class_var) # I am a Class Variable in Class A
print(b.class_var) # Instance var in Class A
print(b.class_var2) # I am a Class Variable in Class B
#once a time a class variable is overridden by an instance variable,
# it will not be accessible by the object of that class. 
# It will be accessible only by the object of the parent class.

class C(A):
    def __init__(self):
        super().__init__() # calling the constructor of the parent class A
        self.var = "I am inside class C's Constructor"
        self.special="Special Variable in Class C"
        self.class_var = "Instance var in Class C"
        super().__init__() # calling the constructor of the parent class A   
a=A()
b=B()
c=C()
print(a.class_var) # I am a Class Variable in Class A
print(b.class_var) # Instance var in Class A    
print(c.class_var) # Instance var in Class C
print(b.class_var2,b.var) # AttributeError: 'B' object has no attribute 'special'             
print(c.special) # Special Variable in Class C
print(c.var,c.class_var,c.special) # I am inside class C's Constructor, Instance var in Class C, Special Variable in Class C
print(super(C,c).class_var) # I am a Class Variable in Class A
print(super().class_var) # I am a Class Variable in Class A