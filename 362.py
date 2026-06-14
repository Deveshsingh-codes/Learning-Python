###FIBONACHI SERIES###
#0 1 1 2 3 5 8 13 21... nextnumber will be th sum of two previous number
def fibonachi_number(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonachi_number(n-1)+fibonachi_number(n-2)
    
number=int(input("Enter the number ="))
print(fibonachi_number(number))    