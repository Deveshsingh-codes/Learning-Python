# Class methods V/s Alternative methods
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
        params=string.split("-")  # ye split dash("-") se split krna start kr dega
        
        
        print(params)    #  ['Karan', '600', 'Teacher']
        
        
        return cls(params[0],params[1],params[2]) 
        #split hui string ke values ko use karke naya Employee object banana aur return karna
        
        
        return cls(*string.split("-"))  
        # * ka matlab hai list ke elements ko alag-alag arguments bana do
        
        
Harry=Employee("Harry",400,"Instructor")
Rohan=Employee("Rohan",500,"Student")
Karan =Employee.from_str("Karan-600-Teacher")
print(Karan.salary)