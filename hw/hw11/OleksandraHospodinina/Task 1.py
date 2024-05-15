class UserException(Exception):
    pass


class User:
    def __init__(self, age:int):
        self.age = age
    def input_age(self):
        #if type(self.age) is not int:
            #raise UserException("Age must be an integer")
        if self.age < 0:
            raise UserException("Age must be a positive number")
        elif self.age % 2 == 0:
            print("Even")
        else:
            print("Odd")
try:
    age = int(input("Enter your age: "))
    age_input = User(age)
    result = age_input.input_age()
except UserException as e:
    print(e)

