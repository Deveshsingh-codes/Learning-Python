###----------*arg and **kwarg in python--------->
def fun_name_print(a, b, c, d):
    print(a, b, c, d)
fun_name_print("Harry", "Devesh", "Surya", "Chhotu") #Function call krdiya
#Its not a scalable function... agr ek naam aur badha diya to ye erro dedega...ese agr ek company ke employees ka krna pdega to bhut bada code bna jayega aur ek achha method nhi hoga 
# the n we use *args


    
def funargs(*args):
        print(*args) #ye puri list print kr dega
        #print(args[0]) ...it prints first element of list 
har=["Harry", "Devesh", "Surya", "Chhotu"] #ye ek conversion bhi jo jaat hai list ka tuple me 
funargs(*har)
# Now its a good method to add employees name in list


#Normal argument--->
def funargs(normal,*args):
    print(normal,*args)
har=["Harry", "Devesh", "Surya", "Chhotu"]  
normal= "I am normal argument and the students are"
funargs(normal,*har)



def funargs(*args):
    for items in args:
        print (items)
har=["Harry", "Devesh", "Surya", "Chhotu"]
funargs(*har)

#<----**kwargs--->

def funarg(normal,*args,**kwargs):
    print(normal)
    print("I would like to introduce")
    for items in args:
        print(items)
    for key, value in kwargs.items():
        print(key,value)
    #for key(f"{key} is a {value}")
har=  ["Harry", "Devesh", "Surya", "Chhotu"] 
normal="I am normal argument and the students are"
kw={"Rohan":"Monitor","Shivan":"programmer","Vineet":"Campus mantri"}
funarg(normal,*har,**kw)
 