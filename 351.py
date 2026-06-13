# Using with block to open python file
#here, in first case these are the normal codes using f.open and close

f=open("Devesh.txt")
print(f.read(4))
f.close()

# here, we ar eusing with blocks...

with open("Devesh.txt") as f:
    a=f.read(4)
    print(a)



#Conclusion --- both are same and give same output 
   