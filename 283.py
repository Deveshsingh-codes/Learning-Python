#Other Functions
mystr = "This is an Elephant"
print(mystr.isalnum()) #it will return false because there are spaces in the string
print(mystr.isalpha()) #it will return false because there are spaces in the string
print(mystr.isdigit()) #it will return false because there are no digits in the string
print(mystr.endswith("Elephant")) #it will return true because the string ends with "Elephant"
print(mystr.endswith("elephant")) #it will return false because the string ends with "Elephant" and not "elephant"
print(mystr.count("s")) #it will return 2 because there are 2 "s" and 3 "e" in the string
print(mystr.capitalize()) #it will return "This is an elephant" because it will capitalize the first letter of the string and make the rest of the letters lowercase
print(mystr.__len__()) #it will return 19 because there are 19 characters in the string including spaces
print(mystr.lower()) #it will return "this is an elephant" because it will convert all the letters in the string to lowercase
print(mystr.upper()) #it will return "THIS IS AN ELEPHANT" because it will convert all the letters in the string to uppercase
print(mystr.replace("Elephant","Tiger")) #it will return "This is an Tiger" because it will replace "Elephant" with "Tiger" in the string
print(mystr.split()) #it will return ['This', 'is', 'an', 'Elephant'] because it will split the string into a list of words
print(mystr.strip()) #it will return "This is an Elephant" because it will remove   any leading and trailing spaces from the string     
print(mystr.swapcase()) #it will return "tHIS IS AN eLEPHANT" because it will swap the case of all the letters in the string
print(mystr.title()) #it will return "This Is An Elephant" because it will capitalize the first letter of each word in the string and make the rest of the letters lowercase    
print(mystr.startswith("This")) #it will return true because the string starts with "This"
print(mystr.startswith("this")) #it will return false because the string starts with "This" and not "this"
print(mystr.strip("This")) #it will return " is an Elephant" because it will    remove "This" from the string