from datetime import datetime, timedelta
import random
import re

#! ================ FIRST TASK
def get_days_from_today(date):

    today = datetime.today().date()

    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()

    except ValueError:
        print("Incorrect date format. Format is YYYY-MM-DD")
        return None

    return (today - date).days


random_date = get_days_from_today("2025-04-11")
print("random date: ", random_date)

user_input = get_days_from_today(input("Enter you date in format: YYYY-MM-DD >>>> "))
print("user-input: ", user_input)

#! =========== SECOND TASK
def get_numbers_ticket(min, max, quantity) -> list:

    try:
        min, max, quantity = int(min), int(max), int(quantity)

    except ValueError as e:
        print("Check input data")
        return []

    else:
        if min < 1 or max > 1000 or min > max or quantity < 1 or quantity > (max - min + 1):
            print("Check your range")
            return []

        uniq_num = []

        while len(uniq_num) < quantity:
            num = random.randint(min, max)

            if num not in uniq_num:
                uniq_num.append(num)

        uniq_num.sort()

    return uniq_num


first_ticket = get_numbers_ticket(78, 100, 20)
print(first_ticket)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

#! =========== THIRD TASK

def normalize_phone(num):

    num = re.sub(r"\D", "", num)

    if num.startswith("380"):
        num = f"+{num}"
    else:
        num = f"+38{num}"

    return num

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

#! =========== FOURTH TASK
def get_upcoming_birthdays(users) :

    coming_birthdays = []
    today = datetime.today().date()

    for user in users:

        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        try:
            birthday_this_year = birthday_date.replace(year=today.year)
        except ValueError:
            birthday_this_year = birthday_date.replace(year=today.year, day=28)

        if birthday_this_year.weekday() > 4:
            birthday_this_year += timedelta(days=7 - birthday_this_year.weekday())

        if birthday_this_year < today:
            try:
                birthday_this_year = birthday_date.replace(year=today.year + 1)
            except ValueError:
                birthday_this_year = birthday_date.replace(year=today.year + 1, day=28)

        if birthday_this_year.weekday() > 4:
            birthday_this_year += timedelta(days=7 - birthday_this_year.weekday())

        if today <= birthday_this_year <= today + timedelta(days=6):
            coming_birthdays.append({"name": user["name"], "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")})

    return coming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Mary", "birthday": "1990.11.05"},
    {"name": "Mike Krav", "birthday": "1990.11.07"},
    {"name": "Vova", "birthday": "1990.11.08"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
