a = input("What is your name")

b = input("How much do u earn")
if int(b)==0:
    raise ZeroDivisionError("b is zero so stopping the program")

if a.isnumeric():
    raise Exception("Numbers are not allowed") 

#output is --->>>
# 
# What is your name43
#Traceback (most recent call last):
#  File "/Users/deveshsingh/Documents/GitHub/Learning-Python/503.py", line 4, in <module>
#    raise Exception("Numbers are not allowed")
#Exception: Numbers are not allowed

# 1000 lines taking 1 hr

print(f"Hello {a}")


# Error

video_link="https://youtu.be/BGQhccSWYpk?si=n1zdh6e35D4JGkcR"          #Visit comment section


c = input()
try:
    print(a)
except Exception as e:
    if c=="harry":
        raise ValueError("Harry is not allowed.")
    print("Exception handled.")