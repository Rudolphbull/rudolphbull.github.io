# Programmer-Mr.OlayinkaGoodluck
#  Student-ID-2144303.


try:
    x = int(input("Enter any number: "))
    y = int(input("Enter another number: "))

    if x != y and x > y:
        print(f'{x} is not equal to {y}.')
        print(f'{x} is bigger than {y}.')
    elif x != y and x < y:
        print(f'{x} is less than {y}.')
        print(f'{x} is not equal to {y}.')
    else:
        print(f'{x} is equal to {y}.')
except ValueError:
    print("Invalid input!!!can only enter digits, and not letters or decimal.")

