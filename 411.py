#Multilevel Inheritance
class Dad:
    pass

class Son(Dad):
    pass

class Grandson(Son):
    pass

#here, Multilevel inheritance is works like---Dad-->Son-->Grandson, Ek dusre se class define ki hai....

class Dad:
    basketball=1
class Son(Dad):
    dance=1
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"
class Grandson(Son):
    dance=6
    def isdance(self):
        return f"Yes I dance {self.dance} no of times" 
    # multile inheritance me agar same function hai to jo last class me define kiya hai wahi call hoga, 
    # jaise yaha pe Grandson class me dance function define kiya hai to wahi call hoga, 
    # Son class ka dance function call nahi hoga.