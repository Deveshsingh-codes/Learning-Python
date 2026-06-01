Box=["Pen","Pencil","Eraser"]
print(Box)
print(Box[0]) #it will print "Pen" because it is the first element in the list
print(Box[1]) #it will print "Pencil" because it is the second element in the list
print(Box[2]) #it will print "Eraser" because it is the third element in the list
print(Box[-1]) #it will print "Eraser" because it is the last   element in the list
print(Box[-2]) #it will print "Pencil" because it is the second last            

Numbers=[1,2,3,4,5,6,7,8,9,10]
print(Numbers)
Numbers.sort() #it will sort the list in ascending order
print(Numbers)
Numbers.sort(reverse=True) #it will sort the list in descending order
Numbers.reverse() #it will reverse the order of the list
print(Numbers)

#Slicing
 
print(Numbers[0:5]) #it will print the first 5 elements in the list
print(Numbers[5:]) #it will print the elements from index 5 to the end of the list
print(Numbers[:5]) #it will print the first 5 elements in the list  
print(Numbers[::2]) #it will print every second element in the list
print(Numbers[1::2]) #it will print every second element in the list starting from index 1
print(Numbers[::-1]) #it will print the list in reverse order   
Numbers.append(11) #it will add 11 to the end of the list
Numbers.insert(0,0) #it will insert 0 at index 0 in the list
Numbers.remove(5) #it will remove 5 from the list   
Numbers.pop() #it will remove the last element from the list
print(Numbers)

#Mutable and Immutable data types in python
#Mutable data types are those data types that can be changed after they are created. For example    lists, sets, dictionaries are mutable data types in python.
#Immutable data types are those data types that cannot be changed after they are created. For example strings, tuples, frozensets are immutable data types in python.       
tp=(1,2,3,4,5) #it will create a tuple with the given elements
print(tp)
tp[1]=77 #it will give an error because tuples are immutable data types in python

#Swapping of two numbers in python
a=10
b=20
print("Before swapping a=",a,"b=",b)
a,b=b,a #it will swap the values of a and b
print("After swapping a=",a,"b=",b)