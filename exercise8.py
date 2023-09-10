from datetime import datetime

user_birthday = input("Enter your birthday\n")

user_birthday_date = datetime.strptime(user_birthday, "%d.%m.%Y")
current_date = datetime.now()

time_till_birthday = user_birthday_date - current_date
print(time_till_birthday)