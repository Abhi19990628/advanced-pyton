# class Abhishek:
#     def __init__(self):
#         self.a = int(input("Enter your first number: "))
#         self.b = int(input("Enter your second number: "))

#     def divide(self):
#         try:
#             result = self.a // self.b
#             print(result)
#         except ZeroDivisionError:
#             print("Error: Division by zero is not allowed.")
#         except ValueError:
#             print("Error: Invalid input. Please enter integer values.")
#         except Exception as e:
#             print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     abhishek_instance = Abhishek()
#     abhishek_instance.divide()
#     print("Abhishek")


class abhishek:
    def __init__(self):
        self.a = int(input("please enter your frist no :"))
        self.b = int(input("please enter your Secound no :"))
    def devide(self):
        try:
            result = self.a // self.b
            print(result)
        except Exception as obj:
            print(f"The main problem on this code {obj}")
             
             
if __name__ == "__main__":
    abhishek_instance = abhishek()
    abhishek_instance.devide()
    
print("there is secound part 8273814047")


class School:
    def __init__(self):
        self.name = input("Please enter your first name: ")
        self.lastname = input("Please enter your second name: ")

    def large(self):
        try:
            fullname = self.name + " " + self.lastname
            if len(self.name) > len(self.lastname):
                print(fullname)
            else:
                print(f"{fullname} (Last name is longer or equal in length to the first name)")
        except Exception as obj:
            print(f"I know I see this problem: {obj}")

if __name__ == "__main__":
    abhishek_instance = School()
    abhishek_instance.large()
    
print("Hi buddy")
