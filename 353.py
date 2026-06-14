#Scope, Global variable and Global Keywords 
def function1(n):
    print(n,"I have printed")

function1("This is me")

l=10 #Global variable
def function2(p):
    l=5 #local variable
    m=8
    print(l,m)
    print(p,"I have printed")
print(l)      # phle local scope dhundhega fir global me dhundhne jayega
#Agr mujhe global variable chnage krna hai to 
l=l+45 #can't open file 'C:\\Users\\DELL\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe': [Errno 22] Invalid argument....error dega
#isko change krne ke liye we use global keywords-----

l = 10  # Global variable

def function2():
    global l

    l = l + 45      # Global: 10 -> 55

    m = l           # Local variable ko global ki new value de di

    print("Global l =", l)
    print("Local m =", m)

function2()

print("Function ke baad Global l =", l)