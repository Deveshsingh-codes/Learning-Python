# Public, Private, and Protected Access specifiers in Python

protected_variable = "This is a protected variable"
# Us class me to use ho hi pr aage banne bali ya fir is se derived aur bhi class me use ho sakta hai,
# lekin bahar se access nahi ho sakta.

_protected =9 # we use single underscore to define a protected variable in python.

private_variable = "This is a private variable"
# Isko sirf specific class me hi use kar sakte hai,
# aur isko bahar se access nahi kar sakte hai.

__private = 10 # we use double underscore to define a private variable in python.

class Employee():
    var = 19  #This is a public variable, we can access it anywhere in the program.
    no_of_games = 4
    _protected=9 # This is a protected variable, we can access it in the class and in the derived class but not outside of the class.
    __private=10  #This is a private variable, we can access it only in the class and not outside of the class or in the derived class.
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    
    def printdetails(self):
        return f"The name is {self.name}, salary is {self.salary}, role is {self.role}"
     
emp = Employee("Harry",400,"Instructor")
print(emp.var) #19
print(emp._protected) #9
print(emp._Employee__private) #10  # THis is called name mangling, ---> Class ka naam fir double underscore fir variable ka naam, isse hum private variable ko access kar sakte hai.
