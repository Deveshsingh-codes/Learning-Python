# Functions and Docstrings
#a=8
#b=18
#c=sum((a,b))  #Built-in function sum() to add a and b
#print(c)  #Output: 26

#def function1():
#    """This is a simple function that prints a message."""
#    print("Hello, this is function1!")
#    print("This function demonstrates the use of docstrings.")
#    print(function1) #This will print the function object, not the docstring that will be nothing right now in the function1() output
#    #function1.__doc__ = "This is a simple function that prints a message." #Assigning a docstring to the function1

def function2(a,b):
    avg = (a + b) / 2
    print(avg)
    return avg
v=function2(5,7)
print(v)
"""This is a function which will calculate the average of two numbers a and b, and return the result."""
print(function2.__doc__) #This will print the docstring of function2, which is the string that describes what the function does.    
