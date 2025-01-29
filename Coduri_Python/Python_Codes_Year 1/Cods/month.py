import calendar

year = int(input('Introduceti anul: '))
month = int(input('Introduceti luna: '))

calendar = calendar.month(year, month)

print(calendar)