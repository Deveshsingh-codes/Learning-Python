 # CLASS METHODS IN PYTHON
 
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
Harry=Employee("Harry",400,"Instructor")
Rohan=Employee("Rohan",500,"Student")

Harry.change_leaves(34)
Employee.change_leaves(90)   #Ye bhi same class variable ko modify kar raha hai
print(Harry.no_of_leaves)  # 90 

#<----------------confusssion----------->

Harry.change_leaves(34)
Employee.change_leaves(90)   #Ye bhi same class variable ko modify kar raha hai
Rohan.change_leaves(50)
print(Harry.no_of_leaves) 
    
#internally Employee.change_leaves(60) ban jata hai To class variable fir se update:Employee.no_of_leaves = 60
#Ab Harry aur Rohan dono ke liye value 60 hai....
#Output = 50