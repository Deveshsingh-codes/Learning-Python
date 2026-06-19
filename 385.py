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



def executor(func):
    func("this")
    
## Function ke andr function daal skte hai as an argument
executor(print)


def dec1(fun1):
    def nowexec():
        print("Executingnow")
        fun1()
        print("Executed")
    return nowexec    