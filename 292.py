# Dictionary and Its functions
d1={"one":1,"two":2,"three":3}

print(type(d1))

print(d1["one"]) #it will print the value of the key "one" which is 1

print(d1["two"]) #it will print the value of the key "two"   

print(d1.get("three")) #it will print the value of the key "three" which is 3

print(d1.get("four")) #it will print None because the key "four" is not present in the dictionary

d1["four"]=4 #it will add the key "four" with the value 4 to the dictionary

print(d1)       

del d1["two"] #it will delete the key "two" from the dictionary

print(d1.update({"five":5}) ) #it will add the key "five" with the value 5 to the dictionary ....it gives none because the update function does not return anything        

d1.update({"six":6}) #it will add the key "six" with the value 6 to the dictionary

print(d1)
