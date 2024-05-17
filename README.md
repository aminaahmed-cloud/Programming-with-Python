# Python Exercises

This repository contains Python exercises covering various topics such as working with lists, dictionaries, classes, functions, dates, spreadsheets, REST APIs, and more. Each exercise is designed to help you practice and improve your Python programming skills.

## Step 1: Working with Lists

Using the provided list `my_list`, write a program that:
1. Prints all elements of the list that are higher than or equal to 10.
2. Creates a new list containing elements higher than or equal to 10 and prints it.
3. Asks the user for a number and prints a list containing elements higher than the user-provided number.

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

Using the provided dictionary employee, write a program that:

1. Updates the job to "Software Engineer".
2. Removes the "age" key from the dictionary.
3. Loops through the dictionary and prints key-value pairs

```python
# Exercise 2 code here
```

## Step 3: Working with List of Dictionaries

Using a list of dictionaries employees, write a program that:

1. Prints the name, job, and city of each employee.
2. Prints the country of the second employee directly.

```
# Exercise 3 code here
```

## Step 4: Working with Functions

Write functions to:

1. Print the name and age of the youngest employee from a list of dictionaries.
2. Calculate the number of upper and lower case letters in a string.
3. Print even numbers from a provided list.

```
# Exercise 4 code here
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
