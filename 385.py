#Decorators in python 
def fun1():
    print("Subscribe now")
    
fun2=fun1 ##()---agr ye paranthisis lga diya to function call ho jayega...
#abhi ye same output dega because fun2 me phl ehi copy ho chuka hai...
fun2()



def funcret(num):
    if num ==0:
        return print
    if num ==1:
        return int
        #return sum  ##Function ka use krke function bhi call kr skte hai..
a=funcret(1) ## <class' int>
a=funcret(0) ## <built-in function print>
print(a)
