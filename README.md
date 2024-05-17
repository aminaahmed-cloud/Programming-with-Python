# Python Exercises

This repository contains Python exercises covering various topics such as working with lists, dictionaries, classes, functions, dates, spreadsheets, REST APIs, and more. Each exercise is designed to help you practice and improve your Python programming skills.

## Step 1: Working with Lists

Using the following list:
```
my_list = [1, 2, 2, 4, 4, 5, 6, 8, 10, 13, 22, 35, 52, 83]
```
1. Write a program that prints out all the elements of the list that are higher than or equal to 10.

2. Instead of printing the elements one by one, make a new list that has all the elements higher than or equal to 10 from this list in it and print out this new list.

3. Ask the user for a number as input and print a list that contains only those elements from my_list that are higher than the number given by the user.

```python
# Print out elements higher than or equal to 10
my_list = [1, 2, 2, 4, 4, 5, 6, 8, 10, 13, 22, 35, 52, 83]
for number in my_list:
    if number >= 10:
        print(number)

# Make a new list with all elements higher than or equal to 10 and print it out
my_new_list = []
for number in my_list:
    if number >= 10:
        my_new_list.append(number)
        print(my_new_list)

# User input as a number and print a list that contains only those elements from my_list that are higher than the number given by the user.
user_input = input("Enter a number: ")
for number in my_list:
    if number > int(user_input):
        my_new_list.append(number)
        print(my_new_list)
```

## Step 2: Working with Dictionaries

1. Using the following dictionary:

employee = {
  "name": "Tim",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer"
}

2. Write a Python Script that:

- Updates the job to Software Engineer
- Removes the age key from the dictionary
- Loops through the dictionary and prints the key:value pairs one by one


```python
# Update the job to Software Engineer

employee = {
    "name": "Amina",
    "age": 27,
    "birthday": "1996-09-22",
    "job": "DevOps Engineer"
}

employee["job"] = "Software Engineer"
print(employee)

# Remove the age key from the dictionary
employee.pop("age")
print(employee)

# Loop through the dictionary and print the key:value pairs one by one
for key, value in employee.items():
    print(f"{key}:{value}")

```


3. Using the following 2 dictionaries:

dict_one = {'a': 100, 'b': 400} 
dict_two = {'x': 300, 'y': 200}

4. Write a Python Script that:

- Merges these two Python dictionaries into 1 new dictionary.
- Sums up all the values in the new dictionary and prints it out
- Prints the max and minimum values of the dictionary


```
# Merge these two python dictionaries into 1 new dictionary
dict_one = {'a': 100, 'b': 400}
dict_two = {'x': 300, 'y': 200}

dict_merged = dict_one.copy()
dict_merged.update(dict_two)
print(dict_merged)

# Sum up all the values in the new dictionary and print it out

sum_of_values = 0
for value in dict_merged.values():
    sum_of_values =sum_of_values + value
print(sum_of_values)

# Print the max and minimum values of the dictionary

merged_values = []
for value in dict_merged.values():
    merged_values.append(value)

merged_values.sort()
print(f"min value: {merged_values[0]}")
print(f"max value: {merged_values[len(merged_values)-1]}")
```



## Step 3: Working with List of Dictionaries

Using a list of 2 dictionaries:
```
employees = [{
  "name": "Tina",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer",
  "address": {
    "city": "New York",
    "country": "USA"
  }
},
{
  "name": "Tim",
  "age": 35,
  "birthday": "1985-02-21",
  "job": "Developer",
  "address": {
    "city": "Sydney",
    "country": "Australia"
  }
}]
```

1. Write a Python Program that:

- Prints out - the name, job and city of each employee using a loop. The program must work for any number of employees in the list, not just 2.
  
- Prints the country of the second employee in the list by accessing it directly without the loop.

```
# Print out - the name, job and city of each employee using a loop. The program must work for any number of employees in the list, not just 2
employees = [{
  "name": "Tina",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer",
  "address": {
    "city": "New York",
    "country": "USA"
  }
},
{
  "name": "Tim",
  "age": 35,
  "birthday": "1985-02-21",
  "job": "Developer",
  "address": {
    "city": "Sydney",
    "country": "Australia"
  }
}]

for employee in employees:
    print(f"name: {employee['name']}")
    print(f"job: {employee['job']}")
    print(f"city: {employee['address']['city']}")
    print("--------------------------")
#  Prints the country of the second employee in the list by accessing it directly without the loop.

country = employees[1]["address"]["country"]
print(f"country of the second employee: {country}")
```


## Step 4: Working with Functions

Write functions to:

1. Print the name and age of the youngest employee from a list of dictionaries.
2. Calculate the number of upper and lower case letters in a string.
3. Print even numbers from a provided list.

**Functions in main.py**

```
# Write a function that accepts a list of dictionaries with employee age and prints out the name and age of the youngest employee
employees = [{
  "name": "Tina",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer",
  "address": {
    "city": "New York",
    "country": "USA"
  }
},
{
  "name": "Tim",
  "age": 35,
  "birthday": "1985-02-21",
  "job": "Developer",
  "address": {
    "city": "Sydney",
    "country": "Australia"
  }
}]

def print_employee_info(employees):
    youngest_employee_age = employees[0]["age"]
    youngest_employee_name = employees[0]["name"]
    for employee in employees:
        if employee["age"] < youngest_employee_age:
            youngest_employee_age = employee["age"]
            youngest_employee_name = employee["name"]

    print(f"name of the youngest employee: {youngest_employee_name}")
    print(f"age of the youngest employee: {youngest_employee_age}")

print_employee_info(employees)

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

count_upper_and_lower_letters("sWWbb137WATbfgdbWb")

# Write a function that prints the even numbers from a provided list

def print_even_numbers(numbers_list):
    for number in numbers_list:
        if number % 2 == 0:
            print(number)
print_even_numbers([0, 3, 9, 10, 2, 13, 120])
```

**Function in helper module**

For cleaner code, declare these functions in its own helper Module and use them in the main.py file

_helper.py_

```
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
```

_main.py_

```
from helper import print_employee_info, count_upper_and_lower_letters, print_even_numbers

employees = [{
    "name": "Tina",
    "age": 30,
    "birthday": "1990-03-10",
    "job": "DevOps Engineer",
    "address": {
        "city": "New York",
        "country": "USA"
    }
},
    {
        "name": "Tim",
        "age": 35,
        "birthday": "1985-02-21",
        "job": "Developer",
        "address": {
            "city": "Sydney",
            "country": "Australia"
        }
    }]

print_employee_info(employees)
count_upper_and_lower_letters("sWWbb137WATbfgdbWb")
print_even_numbers([0, 3, 9, 10, 2, 13, 120])
```


## Step 5: Python Program 'Calculator'

Write a simple calculator program that:

- Takes user input of 2 numbers and an operation.
- Handles plus, minus, multiply, and divide operations.
- Keeps track of the number of calculations.

```
# Exercise 5 code here
```

## Step 6: Python Program 'Guessing Game'

Write a program that:

- Runs until the user guesses a number.
- Generates a random number and asks the user to guess it.
- Prints feedback based on the user's guess.

```
# Exercise 6 code here
```

## Step 7: Working with Classes and Objects

Create classes for Student, Professor, and Lecture. Implement methods to handle data related to students, professors, and lectures

```
# Exercise 7 code here
```

## Step 8: Working with Dates

Write a program that:

- Accepts user's birthday as input.
- Calculates remaining days, hours, and minutes till the birthday.

```
# Exercise 8 code here
```

## Step 9: Working with Spreadsheets

Write a program that reads and sorts employee data from a spreadsheet file.

```
# Exercise 9 code here
```

## Step 10: Working with REST APIs

Write a program that connects to the GitHub API, fetches public repositories for a specific user, and prints their names and URLs.

```
# Exercise 10 code here
```
