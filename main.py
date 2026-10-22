def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        return "Error: Cannot divide by zero!"
    return a/b

def km_to_miles(km):
    return round(km*0.621371,3)

def celsius_to_fahrenheit(celsius):
    return (celsius*9/5)+32

def kg_to_pounds(kg):
    return round(kg*2.20462,3)


def userr_num(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")


