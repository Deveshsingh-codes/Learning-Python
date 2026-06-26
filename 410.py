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
    no_of_games = 4
    def __init__(self,name,game):
        self.name=name 
        self.game = game         
        
    def printdetails(self):
        return   