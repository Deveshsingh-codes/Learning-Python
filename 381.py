#How Import work in python 
#import sklearn as sk 
#print(sk.__version__)
import sys
print(sys.path)

import file2
file2.a

from file2 import a
print(a) #is se compilor confuse ho ajyega aur kisi bhi file ka a print kr dega...

import file2
print(file2.a)
file2.printjoke("This is me")