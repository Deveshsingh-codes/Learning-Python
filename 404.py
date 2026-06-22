#Self and __init__()  [Constructor]

class Employee():
    no_of_leaves=8
    def printdetails(self): 
        # self means ek esa object jiski hm baat kr rhe hai
        # ek instance jis pe function lgaya ja rha hai ....
        return f"Name is {self.name} salary is {self.salary} and role is  {self.role}"
Harry=Employee()
Rohan=Employee()

Harry.name="Harry"
Rohan.name="Rohan"
Harry.salary=400
Rohan.salary=500
Harry.role="Instructor"
Rohan.role="Student"

print(Rohan.printdetails())    # in this function Rohan is entered as an Argument......self=Rohan
#   Name is Rohan salary is 500 and role is  Student



#Harry=Employee("Harry",400,"Instructor")
#print(Harry.salary)
# THis line give an error ---> TypeError: Employee() takes no arguments

        