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
