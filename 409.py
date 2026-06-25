class Employee():
    no_of_leaves=8
    
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The name is {self.name}, salary is {self.salary}, role is {self.role}"
    
    @classmethod
    def from_str(cls,string):
        return cls(*string.split("-"))
    
    @staticmethod
    def printgood(string):
            print("This is a good " + string)
class programmer(Employee):
    def printprog(self):
        return f"The programer name is {self.name} , the salary is {self.salary} and the role is {self.role} . "
Harry=Employee("Harry",400,"Instructor")
Rohan=Employee("Rohan",500,"Student")
Karan =Employee.from_str("Karan-600-Teacher")
Subham = programmer("Subham",700,"Programmer")
Ritik = programmer("Ritik",900,"Programmer")
print(Ritik.printdetails())     # The name is Ritik, salary is 900, role is Programmer

class programmer(Employee):
    def __init__(self,aname,aslary,arole,alanguage):
        self.name=aname
        self.salary=aslary
        self.role=arole
        self.language=alanguage
Harry=Employee("Harry",400,"Instructor")
Rohan=Employee("Rohan",500,"Student",)
Karan =Employee.from_str("Karan-600-Teacher")
Subham = programmer("Subham",700,"Programmer","French")
Ritik = programmer("Ritik",900,"Programmer","java")
print(Subham.printprog())
print(Ritik.printprog())
