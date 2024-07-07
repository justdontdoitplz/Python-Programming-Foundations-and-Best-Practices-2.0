from datetime import datetime, timedelta

TODAY = datetime.now().date()

def get_upcoming_birthdays(users):
    upcoming_birthdays = []
    for user in users:
        birthday_date = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        birthday_this_year = birthday_date.replace(year=TODAY.year)
        
        if birthday_this_year > TODAY:
            delta_today_birthday_date = (birthday_this_year - TODAY).days
            if delta_today_birthday_date <= 7:
                birthday_date_weekday = birthday_this_year.weekday()
                if birthday_date_weekday in [5, 6]:
                    congratulation_date = birthday_this_year + timedelta(days=-birthday_this_year.weekday(), weeks=1)
                    
                    upcoming_birthdays.append(
                        {
                            'name': user['name'],
                            'congratulation_date': congratulation_date.strftime('%Y.%m%.%d')
                        }
                    )
                else:
                        upcoming_birthdays.append(
                            {
                                'name': user['name'],
                                'congratulation_date': birthday_this_year.strftime('%Y.%m%.%d')
                            }
                        )
                        
    return upcoming_birthdays

if __name__ == '__main__':
    users = [
        {"name": "John Doe", "birthday": "1985.07.13"},
        {"name": "Jane Smith", "birthday": "1990.08.27"}
    ]

    upcoming_birthdays = get_upcoming_birthdays(users)

    print("Список привітань на цьому тижні:", upcoming_birthdays)