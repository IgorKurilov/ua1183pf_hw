def check_age():
    try:
        age = int(input("Enter your age please: "))
        if age < 0:
            raise ValueError("ERROR! Age can't be negative")
        if age % 2 == 0:
            print("Your age is even.")
        else:
            print("Your age is odd.")
    except ValueError as valeror:
        print("Chekout:", valeror)

if __name__ == "__main__":
    check_age()