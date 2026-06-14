###PALINDROM NUMBER###
##Palindrome Number woh number hota hai jo aage se aur piche se padhne par same rahe.
#
#Examples:
#
#✅ Palindrome Numbers:
#
#121 → ulta karne par 121
#1221 → ulta karne par 1221
#12321 → ulta karne par 12321
#7 → ulta karne par 7

def palindrome_iterative(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10

    if original == reverse:
        return True
    else:
        return False


number = int(input("Enter a number: "))

if palindrome_iterative(number):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
    
    
    
##<---------------Recursive method------------->
def reverse_number(num, rev=0):
    if num == 0:
        return rev

    return reverse_number(num // 10, rev * 10 + num % 10)


def palindrome_recursive(num):
    return num == reverse_number(num)


number = int(input("Enter a number: "))

if palindrome_recursive(number):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

#Iterative approach → while loop use karti hai.
#Recursive approach → function khud ko call karta hai jab tak base condition (num == 0) na aa jaye.