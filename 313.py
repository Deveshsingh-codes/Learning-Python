# Break statement in Python
#i=0
#while(True):
#    print(i+1,end=" ")
#    if(i==5):
#        break#break statement is used to exit the loop when a certain condition is met. In this case, the loop will continue until i equals 5, at which point it will break out of the loop.
#    i=i+1
#    
    
i=0
while(True):
    if i+1<10:
        i=i+1
        continue #continue statement is used to skip the current iteration of the loop and move on to the next iteration. In this case, if i+1 is less than 10, it will increment i and skip the rest of the loop body, effectively printing only numbers from 1 to 9.
    print(i+1,end=" ")
    if(i==15):
        break
    i=i+1
       