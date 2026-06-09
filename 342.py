#File Writing
f=open("Devesh.txt","rb") #it gives output in binary formate
f=open("Devesh.txt","rt")
content=f.read(3)
print(content)
f.close() # Ek baar agr koi file open kri hai to usko close bhi krna pdt hi hai....

f=open("Devesh.txt","rt")
content=f.read()
for line in content:
    print(line) #this print one text in one line 
for line in f:
    print(line,end="")
print(f.readline())
print(f.readline())

print(f.readlines())
f.close()

    