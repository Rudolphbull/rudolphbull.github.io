

try:
    my_number = int(input('Please enter your number: '))
    i = my_number + 11 #adding 10 to the number since the last number will not be called.
    print(f'Result is: ')
    for i in range(my_number, i, 1): #looping through the entered number incrementing by 1
        print(i)
except ValueError:
    print("Invalid Input")