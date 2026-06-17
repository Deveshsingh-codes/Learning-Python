# Time MOdule in python
import time

initial=time.time()
print(initial)
k=0
while(k<45):
    print("hey")
    k+=1
print(time.time()-initial) #The time in which while loop execute.

initial2=time.time()
for i in range(1):
    print("This is harry bhai.")
print("For loop ran in ",time.time()-initial2)

    