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