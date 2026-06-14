## Recursions :Recursive vs iterative approach
def print2(str1):
    print(str1)
    print("this is  " + str1)
print2("devesh") 

#<------------iterative method--------->
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

#<-------Recursive method----->
def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return n*factorial_recursive(n-1)
number = int(input("Enter the number ="))
print(factorial_recursive(number))


###WORKING###
#5*factorial_recursive(n-1)
#5*4*factorial_recursive(n-1)
#5*4*3*factorial_recursive(n-1)
#5*4*3*2*factorial_recursive(1)....#factorial_recursive(1)==1
