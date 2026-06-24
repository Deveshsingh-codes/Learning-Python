# Static method
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
        
        #return 98 ---------
                                                                     
# Ek esa function bnana hai jo na self ko as an argument le
#na class ko ...khud apne aap me kaam kre...

        
Harry=Employee("Harry",400,"Instructor")
Rohan=Employee("Rohan",500,"Student")
Karan =Employee.from_str("Karan-600-Teacher")
print(Karan.printgood("Harry")) 

#This is a good Harry
#None      -----> isne kuc bhi return nhi kiya is liye none aaya output me 

# ----------Ab ye none ki jgh 98 dega--->
