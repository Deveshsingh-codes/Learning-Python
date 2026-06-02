# Set in python 
S1=set()
print(type(S1))

S1_from_list=set([1,2,3,4,5])
print(S1_from_list)

S1.add(6) #it will add the element 6 to the set S1
S1.add(7)
S1.add(8)
S1.add(8)
S1.add(8)
S1.add(8)
S1.add(8)
S1.add(9)
S1.add(10)
print(S1)

S1.union({6,7,8,9,10,11,12}) #it will return a new set which is the union of S1 and the set {6,7,8,9,10,11,12}
print(S1)

S1={1,2,3,4,5}
S2={4,5,6,7,8}
print(S1.isdisjoint(S2)) #it will return True if the sets have no elements in common

S1.remove(5) #it will remove the element 5 from the set S1
print(S1)   
