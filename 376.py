#Enumerate Function
l1=["Bhindi","Aloo","Tea","Soap","Bag"]

i=1
for item in l1:
    if i%2!=0: 
        print(f"{item}")
    i+=1
    
    
    
for index, item in enumerate(l1):
    if index%2==0:
        print(f"Jarvis please buy{item}")
    