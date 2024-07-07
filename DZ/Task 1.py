import datetime

def get_days_from_today(date):
    current_date = datetime.datetime.now().date()
    date = datetime.date.fromisoformat(date)
    return (current_date - date).days
