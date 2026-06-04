print("Num1")
Num1 = input()
print("Num2")
Num2 = input()
#print("Sum", int(Num1) + int(Num2))
#print("This is very imp program")

try:
    print("Sum", int(Num1) + int(Num2))
except Exception as e:
    print(e) #This will print the error message if there is an exception, for example if the user enters a non-integer value for Num1 or Num2, it will raise a ValueError and the error message will be printed.
print("This is very imp program") #this will print even th eprogram is invaid because we have handled the exception and the program will continue to run without crashing.

