#Faulty Calculator  

#PYTHON TASK -  Write a program to create a calculator which will correctly solve all the problems except the following ones:   
#87 + 45 = 555
#56 * 9 = 45    
#56 / 6 = 4

print("Enter the first number:\n ")
num1 = int(input())
print("Enter the second number:\n ")
num2 = int(input())
print("Enter the operator: ")
operator = input()
if num1 == 87 and num2 == 45 and operator =="+":
    print("Result:  555")
elif num1 == 56 and num2 == 9 and operator =="*":
    print("Result:  45")
elif num1 == 56 and num2 == 6 and operator =="/":
    print("Result:  4")
elif operator == "+":
    print("Result:",num1 + num2)
elif operator == "-":
    print("Result:",num1 - num2)
elif operator == "*":
    print("Result:",num1 * num2)
elif operator == "/":
    print("Result:",num1 / num2)
else:
    print("Invalid operator")





