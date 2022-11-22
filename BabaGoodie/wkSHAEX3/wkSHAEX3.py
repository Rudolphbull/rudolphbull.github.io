#Programmer-Mr.OlayinkaGoodluck
#Student-ID-2144303.

try:
    your_number = int(input("Enter any number: "))
    if your_number % 2 == 0:
        print("Your number is an even number.")
    else:
        print("Your number is an odd number.")
except ValueError:
    print("Invalid Input: only numbers are allowed")
#     ValueError: invalid literal for int() with base 10: 'a'

