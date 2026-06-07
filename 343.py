# Writing and appending to a file
f=open("Devesh.txt","w") # w se file write mode me khulti hai, agr file exist nhi krti to nayi file create kr dega aur agr file exist krti hai to uske content ko overwrite kr dega
f.write("This is Devesh's file.\n") # write() method se hum file me content likh sakte hai, \n se new line create hoti hai
f.write("I am learning Python.\n")          
f.close() # file ko close krna jaruri hai, taki changes save ho jaye aur memory free ho jaye

        
        
        
        