##Anonymous/Lambda Function in python###
def add(a,b):    #normal code for adding
    return a+b

subtract=lambda x,y:x-y  #subtract function by using lambada
print(9,5)

#<------>
def a_first(a):
    return a[1]
a= [[1,14],[3,56],[3,1]]
a.sort(key=a_first)
print(a)
# same using lambda to sort by the second element
a.sort(key=lambda x: x[1])
print(a)