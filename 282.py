#String Slicing and other functions in python 
#string = Combination of charcters

mystr="This is an Elephant"

print(mystr)
print(mystr[5]) #string indexing starts from 0
print(mystr[:6])#string slicing---[x:y] x is included and y is Excluding function
print(mystr[5:10]) #string slicing
print(mystr[:10:2]) #string slicing with step size (Advance slicing)
print(mystr[::2]) #string slicing with step size (Advance slicing)

#negative slicing

print(mystr[-2:])
print(mystr[-5:-2])
print(mystr[-5:])  
print(mystr[:-5])
print(mystr[-1:-10]) #it will not print anything because -1 is greater than -10
print(mystr[-10:-1]) #it will print from -10 to -1 but not including -1

#Reverse slicing

print(mystr[-1:-10:-1]) #it will print from -1 to -10 but not including -10
print(mystr[-10:-1:-1]) #it will not print anything because -10 is greater than -1
print(mystr[::-1]) #it will print the string in reverse ordergit