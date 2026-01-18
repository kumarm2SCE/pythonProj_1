# Dice role project #
#####################

import random

choice = input("Roll the dice (y/n)").lower()
if(choice=='y'):
    print("random number is:" +  str(random.randint(1,6)))
          
    number1 = input("Enter your first number")
    if( 0< int(number1) >6):
        while (0< int(number1) >6):
            print("Please enter number between 1 and 6")
            number1 = input(">")

    number2 = input("Enter your second number")   
    if( 0< int(number2) >6):
        while (0< int(number2) >6):
            print("Please enter number between 1 and 6")
            number2 = input(">")

    print(f"your number roll is {number1} and next number is {number2}")
    print(f"({number1},{number2})")
else:
    exit

