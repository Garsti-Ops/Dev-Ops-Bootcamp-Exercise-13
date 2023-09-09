def findYoungestEmployeeAndPrintData(employees):
    youngestEmployeeId = 0
    age = 0
    id = 0

    for employee in employees:
        if id == 0:
            age = employee["age"]

        if age > employee["age"]:
            age = employee["age"]
            youngestEmployeeId = id

        id += 1

    print(employees[youngestEmployeeId]["age"])


def calculateUpperAndLowerCaseLetters(subject):
    uppercaseLetters = 0
    lowercaseLetters = 0

    for char in subject:
        if char.isupper():
            uppercaseLetters += 1

        if char.islower():
            lowercaseLetters += 1

    print(f"upper case: {uppercaseLetters}, lower case: {lowercaseLetters}")


def printEvenNumbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(number)
