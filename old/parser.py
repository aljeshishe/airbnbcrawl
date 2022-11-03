import json
import re


def parse(text):
    data = json.loads(text)
    months = data['data']['merlin']['pdpAvailabilityCalendar']['calendarMonths']
    for month in months:
        for day in month['days']:
            if day['bookable'] is None:
                continue
            day.update(day['price'])
            del day['price']
            if day['__typename'] != 'MerlinCalendarDayPrice':
                print(f'Unexpected {day}')
            del day['__typename']
            if day['localPriceFormatted'] is not None:
                day['localPriceFormatted'] = re.sub(pattern='\D', repl='', string=day['localPriceFormatted'])
            yield day



if __name__ == '__main__':
    with open('raw_29281986.json') as fp:
        for d in parse(fp.read()):
            print(d)