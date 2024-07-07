from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    current_date = datetime.today().date()
    birthdays_this_week = []

    for user in users:
        name = user['name']
        birthday = datetime.strptime(user['birthday'], "%Y.%m.%d").date()

        birthday_this_year = birthday.replace(year = current_date.year)

        if birthday_this_year < current_date:
            birthday_this_year = birthday_this_year.replace(year = current_date.year + 1)

        if current_date <= birthday_this_year < current_date + timedelta(days = 7):
            birthdays_this_week.append({"name": name, "congratulation_date": get_nearest_workday(birthday_this_year).strftime("%Y.%m.%d")})

    return birthdays_this_week

def get_nearest_workday(date):
    while date.weekday() > 4:
        date = date + timedelta(days=1)
    return date


users = [
    {"name": "John Doe", "birthday": "1985.07.02"},
    {"name": "John Doe2", "birthday": "1985.07.07"},
    {"name": "John Doe3", "birthday": "1985.07.12"},
    {"name": "John Doe4", "birthday": "1985.07.13"},
    {"name": "Jane Smith", "birthday": "1990.07.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
