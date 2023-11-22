
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{self.first}.{self.last}@company.com"

    def fullname(self):
        return f"{self.first.capitalize()} {self.last.capitalize()}"

    def apply_raise(self):
        return round(self.pay * 1.05)
    

emp_1 = Employee("abul", "hossain", 10000)
emp_2 = Employee("razu", "choudhury", 20000)

# print(emp_1.fullname())
# print(emp_1.email)
print(emp_1.pay)
# Employee.apply_raise(emp_1)
emp_1.apply_raise()
print(emp_1.pay)


###############################

while True:
    try:
        user_response = str(input("Please, enter your response here. "))
        if user_response in ["y", "Y", "yes", "Yes", "yep" "Yep", "n", "N", "no", "NO", "nope", "Nope"]:
            break
    except ValueError:
        print("Invalid reaponse.")
    else:
        print("You are welcome!")


while True:
    try:
        user_response = str(input("Please, enter your response here. "))
        if user_response in ["Y", "y", "Yes", "yes", "yep", "Yep", "n", "N", "NO", "Nope", "nope"]:
            break
    except ValueError:
        print("Invalid response.")
    print("You are welcome!")

