from datetime import date, timedelta


def dates(start_date, days):
    if start_date is None:
        start_date = date.today()
    start_date = start_date if isinstance(start_date, date) else date.fromisoformat(start_date)
    base = start_date
    dates = [base + timedelta(days=x) for x in range(days)]
    return list(map(str, dates))


def format_dict(d):
    return ' '.join([f'{k}:{v}' for k,v in d.items()])

