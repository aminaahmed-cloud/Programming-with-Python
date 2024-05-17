def print_employee_info(employees):
    youngest_employee_age = employees[0]["age"]
    youngest_employee_name = employees[0]["name"]
    for employee in employees:
        if employee["age"] < youngest_employee_age:
            youngest_employee_age = employee["age"]
            youngest_employee_name = employee["name"]

    print(f"name of the youngest employee: {youngest_employee_name}")
    print(f"age of the youngest employee: {youngest_employee_age}")


# Write a function that accepts a string and calculates the number of upper case letters and lower case letters

def count_upper_and_lower_letters(string):
    lower_letters = 0
    upper_letters = 0
    for char in list(string):
        if char.islower():
            lower_letters += 1
        elif char.isupper():
            upper_letters += 1
    print(f"number of lower case letters: ", lower_letters)
    print(f"number of upper case letters: ", upper_letters)


# Write a function that prints the even numbers from a provided list

def print_even_numbers(numbers_list):
    for number in numbers_list:
        if number % 2 == 0:
            print(number)
