# Map ,filter and Reduce

# MAP ----> kisi iek function o ek puri list me apply kr deta hai...

number=["3","34","64"]

#number[2]=number[2] + 1
## it gives error 
#Error isliye diya kyunki number[2] ki value "64" string hai aur tum usme 1 (integer) add karne ki koshish kar rahe ho.

for i in range(len(number)):
    number[i]=int(number[i])
number[2]=number[2]+1
print(number[2])



number=["3","34","64"]
#map(int,number)   ---> X
number=list(map(int,number))


def sq(a):
    return a*a
def cube(a):
    return a*a*a
num=[2,3,4,5,6,7,3,3,3,3,2,6]
square=list(map(sq, num))     #yha dono lines ka mtlb same 
square=list(map(lambda x:x*x, num))   #yha dono lines ka mtlb same 
cube=list(map(lambda x:x*x*x,num))
print(square,cube)



def square(a):
    return a*a

def cube(a):
    return a*a*a
func=[square,cube]
