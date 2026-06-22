# INSTANCE AND CLASS VARIABLE

class Employee: #It is an empty class
    pass  # Pass = Nothing

class Employee:
    no_of_leaves=8 # these are the leaves of this class
Harry=Employee()
Rohan=Employee()

Harry.name="Harry"
Rohan.name="Rohan"
Harry.salary=400
Rohan.salary=500
Harry.role="Instructor"
Rohan.role="Student"

print(Harry.salary)  # 400
print(Rohan.salary)  #500
print(Harry.role, Rohan.role) #   Instructor Student


print(Harry.no_of_leaves)   # 8 ----> Class ki property ko Harry ka use krke access kr liya 

Employee.no_of_leaves=9 # now it is changed, only use of Employee. 
print(Harry.no_of_leaves) #  9

Rohan.no_of_leaves=17   # it cann't be chnage
print(Harry.no_of_leaves) #  9

print(Rohan.__dict__)  #  {'name': 'Rohan', 'salary': 500, 'role': 'Student', 'no_of_leaves': 17}  ....it prints the dictionary of Rohan
print(Rohan.no_of_leaves) # Above Rohan's no_of_leaves change it returns 17

