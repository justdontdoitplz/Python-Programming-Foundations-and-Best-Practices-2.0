from datetime import datetime, timedelta

TODAY = datetime.now().date()

def get_days_from_today(date):
    try:
        date = datetime.strptime(date, '%Y-%m-%d').date()
        return int((date - TODAY).days)
    except ValueError as value_error:
        print('plz enter valud format date, in this format for example yyyy-mm-dd')

if __name__ == '__main__':
    input_date = input('input your date plz - ')
    days_from_today = get_days_from_today(input_date)
    
    if days_from_today is not None:
        print(days_from_today)