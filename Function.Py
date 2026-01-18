# def Greet(value1):
#     print(f"This is {value1} test function")
#     print(f"welcome to {value1} your first program")

# Greet("Mukesh")

# Return Function

# def return_GreetFunction(name):
#     return f"This is your value {name}"

# a = return_GreetFunction("Mukesh")
# print(a)

# def increment(number,by=1):
#     return number + by

# print(increment(2),5)

def multiply(*parameter):
    total = 1
    for number in parameter:
        total *= number
    return total

print(multiply(1,2,3,4,5))
    