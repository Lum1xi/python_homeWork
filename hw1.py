

def print_name_age(name, age):
    try:
        age = int(age)
        if  age < 0 or age >= 130:
            raise ValueError("Enter a valid age")
        else:
            print(f"Hi {name}Your age is {age}")

    except ValueError as e:
        print(e)


InputName = input("Enter your name: ")
InputAge = input("Enter your age: ")

print_name_age(InputName, InputAge)