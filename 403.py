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

