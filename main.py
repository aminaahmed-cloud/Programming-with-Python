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
