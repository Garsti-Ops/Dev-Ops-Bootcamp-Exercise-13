employee = {
  "name": "Tim",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer"
}

employee["job"] = "Software Engineer"
print(employee)

del employee["age"]
print(employee)

for key in employee.keys():
    print(f'Key: {key} Value: {employee[key]}')