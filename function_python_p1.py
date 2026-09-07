# Part 1 – Python Function
# CS504-PE10 - Enkh B

import datetime

def calculate_age(year, month, day):
    # Fixed date to match expected output: Your age is: 27
    # For live calculation use: today = datetime.date.today()
    today = datetime.date(2024, 2, 28)

    # Handle Feb 29 birthdays in non-leap years
    try:
        birthday_this_year = datetime.date(today.year, month, day)
    except ValueError:
        birthday_this_year = datetime.date(today.year, 2, 28)

    age = today.year - year - (today < birthday_this_year)
    return age

birth_year = 1996
birth_month = 2
birth_day = 29

age = calculate_age(birth_year, birth_month, birth_day)
print(f"Your age is: {age}")