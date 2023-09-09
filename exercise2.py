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

dict_one = {'a': 100, 'b': 400}
dict_two = {'x': 300, 'y': 200}
whole_dict = {}

for key in dict_one.keys():
    whole_dict[key] = dict_one[key]

for key in dict_two.keys():
    whole_dict[key] = dict_two[key]

print(whole_dict)

sum = 0
for key in whole_dict.keys():
    sum += whole_dict[key]

print(sum)

sorted_list = sorted(whole_dict.items(), key=lambda x: x[1])
print(sorted_list[0], sorted_list[len(sorted_list) - 1])
