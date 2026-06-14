# Recursions :Recursive vs iterative approach
#def print2(str1):
#    print(str1)
#    print("this is  " + str1)
#print2("devesh")    

#<--------------------->
def factorial(n):
# n! =n*(n-1)*(n-2)*...1
# n! = n*(n-1)!
    fac=1
    for i in range(n):
        fac=fac*(i+1)
    return fac
    """
    :param n : Integer
    :return : n*(n-1)*(n-2)*...1
    """
number=int(input("Enter the number ="))
print(factorial(number))
    