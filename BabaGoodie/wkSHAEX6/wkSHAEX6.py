# Programmer-Mr.OlayinkaGoodluck
# Student-ID-2144303.

try:
    number_count = int(input("How many numbers do you have? "))
    number_sum = 0 # assign inputted integer to zero first
    for number in range(number_count): # iterate through the given number count
        given_number = int(input("Enter a number: "))
        number_sum += given_number

    number_count_avg = number_sum / number_count
    new_number_count_avg = round(number_count_avg, 1)
    print(f"The average of the numbers is {new_number_count_avg}")
except ValueError:
    print("Sorry!!!!Invalid Input!!!!numbers only, no decimals")