# Seek(), tell() and readline() methods
f=open("Devesh.txt","r") # r se file read mode me khulti hai
print(f.read()) # read() method se hum file ka content read kar sakte hai
print(f.tell()) # tell() method se hum file pointer ki current position dekh sakte  
print(f.seek(0)) # seek() method se hum file pointer ki position change kar sakte hai, yaha 0 se file pointer ko start me le jate hai
print(f.readline()) # readline() method se hum file ka ek line read kar sakte hai
f.close() # file ko close karna jaruri hai, taki memory free ho jaye


print(f.readline())
f.seek(0)
f.close()
 