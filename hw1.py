name = input("Enter your name: ")
age = input("Enter your age: ")

try:
    age = int(age)
    if  age < 0 or age >= 130:
        raise ValueError("Enter a valid age")
    else:
        print(f"Hi {name}Your age is {age}")

except ValueError as e:
    print(e)