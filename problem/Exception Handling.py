import sys
no_1 = int(input("Enter your frist no : "))
no_2 = int(input("enter your secound no :"))
try:
    div = no_1//no_2
    print(div)
except :
    print(sys.exc_info()[0]) # in exception hadling get information for class
    print(sys.exc_info()[1]) # in Exception handling get infomation 
    


    
# in Execption handling using raise for print error for user 
try:
    age = int(input("Enter your age :"))
    if age < 0:
        raise ValueError()
    print("Your age is :", age)
except ValueError:
    print("plz fillout the real value")
    
print("Everything is good")

# first way to solve



try:
    age = int(input("Enter your age :"))
    if age < 0:
        raise ValueError("plz fill the real value")
    print("Your age is :", age)
    
except ValueError as obj:
    
    print(obj)
    
print("Everything is good")




#user defined Exception handling\
class five_division_error(Exception):
    pass
    
try:
    v1=int(input("Enter your first no :"))
    v2=int(input("Enter your secound no is :"))
    if v2 == 5:
        raise five_division_error("cannot be dividec by 5")
    a=v1//v2
    print(a)

except (five_division_error,ZeroDivisionError) as obj:
    print (obj)
    
print("rest of code")



