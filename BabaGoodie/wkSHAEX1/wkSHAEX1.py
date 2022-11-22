# Programmer-Mr.OlayinkaGoodluck
# Student-ID-2144303.

print("Test Run: ")
print('-' * 15)
# To specify the rate we are expecting from users.
rate = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
confirmed_employee_name = " "
employee_name = input("What is your name? ").title()
# To ensure user does not enter a blank employee name
if len(employee_name) == 0:
    while len(employee_name) == 0:
        employee_name = input("Employee name can not be blank What is your name? ").title()
        if len(employee_name) > 0:
            confirmed_employee_name = employee_name
else:
    confirmed_employee_name = employee_name
# To ensure user does not enter digits in place of employee name
if employee_name.isdigit():
    while employee_name.isdigit():
        employee_name = input("Employee name can not contain number, What is your name? ").title()
        if not employee_name.isdigit():
            confirmed_employee_name = employee_name

else:
    confirmed_employee_name = employee_name
# To ensure user does not enter a blank in place of employee surname
confirmed_employee_surname = " "
employee_surname = input("What is your surname? ").title()
if len(employee_surname) == 0:
    while len(employee_surname) == 0:
        employee_surname = input("Employee surname can not be blank What is your name? ").title()
        if len(employee_surname) > 0:
            confirmed_employee_surname = employee_surname
else:
    confirmed_employee_surname = employee_surname
# To ensure user does not enter digits in place of employee surname
if employee_surname.isdigit():
    while employee_surname.isdigit():
        employee_surname = input("Employee surname can not contain number, What is your name? ").title()
        if not employee_name.isdigit():
            confirmed_employee_surname = employee_surname
else:
    confirmed_employee_surname = employee_surname

confirmed_employee_salary = " "
employee_salary = input(
    f"Hello,{confirmed_employee_name} {confirmed_employee_surname}, can you please input your salary? £")
# To ensure user does not enter a blank in place of employee salary
if len(employee_salary) == 0:
    while len(employee_salary) == 0:
        employee_salary = input(
            f"Hello,{confirmed_employee_name} "
            f"{confirmed_employee_surname}, employee salary can not be blank\n can you please input your salary? £")
        if len(employee_salary) > 0:
            confirmed_employee_salary = employee_salary
else:
    confirmed_employee_salary = employee_salary
# To ensure user does not enter a digit in place of employee salary
if not employee_salary.isdigit():
    while not employee_salary.isdigit():
        employee_salary = int(input("Employee salary can not contain alphabet, What is your salary? "))
    if employee_salary.isdigit():
        confirmed_employee_salary = employee_salary

else:
    confirmed_employee_salary = employee_salary
confirmed_employee_rate = ""
employee_rate = float(input("What is your tax rate? "))
# To ensure the user does not enter a blank for  employee rate
if employee_rate == 0:
    while employee_rate == 0:
        employee_rate = float(input("What is your tax rate? "))
        if employee_rate > 0:
            confirmed_employee_rate = employee_rate
else:
    confirmed_employee_rate = employee_rate
# To ensure the user rate is within the expected rate
if float(employee_rate) not in rate:
    employee_rate = input("Pls enter rate between 0.1 to 0.9 ")
    confirmed_employee_rate = employee_rate
else:
    confirmed_employee_rate = employee_rate

net_salary = (int(confirmed_employee_salary) - (int(confirmed_employee_salary)) * float(confirmed_employee_rate))

print(f"The net salary of {confirmed_employee_name} {confirmed_employee_surname} is £{net_salary}.")
