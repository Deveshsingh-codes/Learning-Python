#  Single inheritance: 
# In single inheritance, a child class inherits from a single parent class.
# This means that the child class can access the attributes and methods of the parent class, 
# allowing for code reuse and organization. Single inheritance is a fundamental concept in object-oriented programming and 
# is widely used in many programming languages.

#<<<------------------>>>

class Employee():
    no_of_leaves=8
    
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The name is {self.name}, salary is {self.salary}, role is {self.role}"
    @classmethod
    def change_leaves(cls,newleave):  # by this method we will access object  by any instance or class
        cls.no_of_leaves=newleave
    @classmethod
    def from_str(cls,string):
        return cls(*string.split("-"))
    
    @staticmethod
    def printgood(string):
            print("This is a good " + string)
class programmer(Employee): # here, (Employee) is the parent class and programmer is the child class
    #and we are inheriting the properties of Employee class in programmer class 
    def printprog(self):
        return f"The programer name is {self.name} , the salary is {self.salary} and the role is {self.role} . "
Harry=Employee("Harry",400,"Instructor")
Rohan=Employee("Rohan",500,"Student")
Subham = programmer("Subham",700,"Programmer")
Ritik = programmer("Ritik",900,"Programmer")
print(Ritik.printdetails())     # The name is Ritik, salary is 900, role is Programmer
print(Ritik.printprog())   #The programer name is Ritik , the salary is 900 and the role is Programmer .

#<-------------------->
class programmer(Employee): 
    def __init__(self, aname, asalary, arole, alanguage): #creating another constructor in child class
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.language = alanguage  #....WARNING........code overidding and code reusibility is not here....
    def printprog(self):
        return f"The programer name is {self.name} , the salary is {self.salary} and the role is {self.role} and the language is {self.language} . "
Harry=Employee("Harry",400,"Instructor")
Rohan=Employee("Rohan",500,"Student")
Subham = programmer("Subham",700,"Programmer",["Python"])
Ritik = programmer("Ritik",900,"Programmer",["C++"])
print(Ritik.printdetails())     # The name is Ritik, salary is 900, role is Programmer
print(Ritik.printprog())   #The programer name is Ritik , the salary is 900 and the role is Programmer and the language is ['C++'] .
print(Subham.printprog())   #The programer name is Subham , the salary is 700 and the role is Programmer and the language is ['Python'] .