# Multiple inharitance

class Employee():
    no_of_leaves=8
    
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The name is {self.name}, salary is {self.salary}, role is {self.role}"
    
    @classmethod
    def from_str(cls,string):
        return cls(*string.split("-"))
    
    @staticmethod
    def printgood(string):
            print("This is a good " + string)

class Player:
    var = 9
    no_of_games = 4
    def __init__(self,name,game):
        self.name=name  # these are the two attributes of the class Player 
        self.game = game         
        
    def printdetails(self):
        return f"The Name is {self.name} and the game is  {self.game}."
class coolprogram(Employee, Player):
    var = 10
    language = "C++"
    def printlanguage(self):
        print(self.language)  
          
Harry = Employee("Harry",400,"Instructor")
Rohan = Employee("Rohan",500,"Student")
Subham = Player("Subham",["Cricket"])
Karan = coolprogram("Karan",900,"Cool Programmer")
det = Karan.printdetails()  # The name is Karan, salary is 900, role is Cool Programmer
print(det)
print(Karan.var)  #10  #ye employee ki class ka var print karega
                       #kyuki coolprogram me var=10 hai aur 
                       #employee me var=9 hai to coolprogram ka var print hoga