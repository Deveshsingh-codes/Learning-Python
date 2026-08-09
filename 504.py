# python 'is' vs '==' : What is difference

# == - value equality - Two object have the same Value
# is - Reference equality - two refernce refer to the same object

#task-->
a=[2,3,"64"]
b=[2,3,"64"]
print(b is a)  

#output-False
# because here both a and b is pointing difference list, here both has allocated memory loacation or addresss