class Empolyee:
    language = "py" # this is class Attribute
    salary = 12000
    
    def get_info(self):
        print(f"the language is {self.language}. the salary is {self.salary}")
        
abhishek = Empolyee()
# name= "abhsihek kumar" # this is and instance attribute
abhishek.get_info()
# print(name,abhishek.language , abhishek.salary)

# ravi = Empolyee
# name = "Ravi kumar"
# print(name , ravi.language , ravi.salary)
class programer(Empolyee):
    language="java"
    
    # def get_info(self):
    #     print(f"the language is {self.language}. the salary is {self.salary}")
        
    
abhi=programer()
abhi.get_info()

