class Student:

    def __init__(self,name:str,age:int,gender:str):
        self.name=name 
        self.age=age 
        self.gender=gender

    def display(self):
        print(f"{self}")
        print(f"Hi My name is {self.name}")

s1=Student("Abhishek",15,"male")


print(s1.name)
s1.display()