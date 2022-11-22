# Programmer-Mr.OlayinkaGoodluck
# Student-ID-2144303.

try:
    def max_of_three_numbers(first_number, second_number, third_number):
        max_number = numbers[0] #setting initial largest number to number in index1
        for number in numbers:
            if number > max_number:
                max_number = number
        print(f"Maximum number: {max_number}")
        return max_number


    first_number = int(input("First number: "))
    second_number = int(input("Second number: "))
    third_number = int(input("Third number: "))
    numbers = [first_number, second_number, third_number]
    max_of_three_numbers(first_number, second_number, third_number)
except ValueError:
    print("Sorry!!!!!number can not be blank, and you can not enter an alphabet, or decimals.")