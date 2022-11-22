# Programmer-Mr.Olayinka Goodluck
# Student-ID-2144303.

all_employee_id = []

unordered_employee_names = []
ordered_employee_names = []


employees_name_and_number_of_properties_sold = {}
number_of_employees = int(input("Enter the number of employees for this week: "))
properties_sold_by_employees = []
employees_sales_commission = []

commission = 500


def employeeDetails(number_of_employees):
    for number in range(number_of_employees):
        while not number_of_employees <= 5:
            if number_of_employees > 5:
                number_of_employees = int(input("Sorry!!!number of employees for this week is between 2 and 5: "))
                if number_of_employees <= 5:
                    employee_name = input("Enter the name of the employee: ").title()
                    if len(employee_name) == 0:
                        while len(employee_name) == 0:
                            employee_name = input("Employee name cannot be blank: ").title()
                            unordered_employee_names.append(employee_name)
                    elif len(employee_name) > 0:
                        unordered_employee_names.append(employee_name)
                    employee_name = input("Enter the name of the employee: ").title()
                    if not employee_name.isalpha():
                        while not employee_name.isalpha():
                            employee_name = input("Please employee name should be alphabets: ").title()
                            if employee_name.isalpha():
                                unordered_employee_names.append(employee_name)
        else:
            employee_name = input("Enter the name of the employee: ").title()
            if not employee_name.isalpha():
                while not employee_name.isalpha():
                    employee_name = input("Please employee name should be alphabets: ").title()
                    if employee_name.isalpha():
                        unordered_employee_names.append(employee_name)

        employee_id = input("Enter the employee id: ")
        # This check if a user enters a non-digit value
        if not employee_id.isdigit():
            while not employee_id.isdigit():
                employee_id = input("Please enter only digits for employee id: ")
                if employee_id.isdigit():
                    all_employee_id.append(int(employee_id))
        else:
            all_employee_id.append(int(employee_id))

        number_of_properties_sold = input("Enter the number of properties sold: ")
        if not number_of_properties_sold.isdigit():
            while not number_of_properties_sold.isdigit():
                number_of_properties_sold = input("Please enter only digits for the number of properties sold: ")
                if number_of_properties_sold.isdigit():
                    properties_sold_by_employees.append(int(number_of_properties_sold))
                    employees_name_and_number_of_properties_sold[employee_name] = int(number_of_properties_sold)
        else:
            properties_sold_by_employees.append(int(number_of_properties_sold))
            employees_name_and_number_of_properties_sold[employee_name] = int(number_of_properties_sold)

        employee_sales_commission = properties_sold_by_employees[number] * commission
        employees_sales_commission.append(employee_sales_commission)





# Check number of employee entered.


expected_number_list = [2, 3, 4, 5]


def checkEnteredNumberOfEmployees(number):
    if number not in expected_number_list:
        while number not in expected_number_list:
            number = int(input
                         ("Number of employees for this week should not be 1\nand any number greater than 5, but between 2 and 5: "))
            # employeeDetails(number)
            if number in expected_number_list:
                employeeDetails(number)
                return number

    else:
        employeeDetails(number)
        return number


# number_of_employees = int(input("Enter the number of employees for this week: "))

number_of_employee_for_the_week = checkEnteredNumberOfEmployees(number_of_employees)

# ###THE OUTPUT STARTS FROM HERE ###
# The sum of property sold by employees

# This is the to arrange the property sold in descending order
properties_sold_by_employees.sort(reverse=True)



for number in range(number_of_employee_for_the_week):
    for name, number_of_property in employees_name_and_number_of_properties_sold.items():
        # This is to arrange the name of employee according highest number of property sold to the lowest
        if number_of_property == properties_sold_by_employees[number]:
            ordered_employee_names.append(name)

# This print out the name in ordered form
print("--- ordered employee name and number of property sold ---")
for number in range(len(ordered_employee_names)):
    print("Employee's name: {}, Number of property sold: {}".format(ordered_employee_names[number],
                                                                    employees_name_and_number_of_properties_sold.get(
                                                                        ordered_employee_names[number])))

# This is to get sale commission for each employee from highest to lowest in a week
print("--Commission for the week--")
for number in range(len(ordered_employee_names)):
    print("Employee's name: {}, commission: £{:.2f}".format(ordered_employee_names[number],
                                                            employees_name_and_number_of_properties_sold.get(
                                                                ordered_employee_names[number]) * commission))


print("for the week total commission: £{:.2f}".format(sum(employees_sales_commission)))

# The sum of property sold
print(f"The sum of property sold: {sum(properties_sold_by_employees)}")

employee_with_most_property_sale = ordered_employee_names[0]

bonus_for_employee_with_most_property_sale_bonus = ((employees_name_and_number_of_properties_sold.get(
    employee_with_most_property_sale) * 15 * commission) / 100)

print(f"bonus_for_employee_with_most_property_sale: £{int(round(bonus_for_employee_with_most_property_sale_bonus, 2))}")

# The employee name and number of property sold most
print(
    f"The name of Employee with most property sale is {employee_with_most_property_sale} and Number of property sold is"
    f" {employees_name_and_number_of_properties_sold.get(ordered_employee_names[0])}. ")

# The bonus applied
bonus_applied = (employees_name_and_number_of_properties_sold.get(employee_with_most_property_sale) * 15) / 100
print(f"The bonus applied is: {bonus_applied}")
