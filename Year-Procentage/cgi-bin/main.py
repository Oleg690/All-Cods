import time
import cgi

params = cgi.FieldStorage()

verify = params.getfirst('verify', 'login')

print('Content-type: text/html\n')

current_time = time.localtime()

year = current_time.tm_year
month = current_time.tm_mon
day = current_time.tm_mday

day = day - 1

result = ''

dates = [
    [1, 31],
    [2],
    [3, 31],
    [4, 30],
    [5, 31],
    [6, 30],
    [7, 31],
    [8, 31],
    [9, 30],
    [10, 31],
    [11, 30],
    [12, 31]
]

x = year % 4

daysInTheYear = 0

if x == 0:
    dates[1].append(29)
    daysInTheYear = 366
else:
    dates[1].append(28)
    daysInTheYear = 365

timePassed = 0


for i in dates:
    if i[0] != month:
        timePassed += i[1]
    else:
        hour = current_time.tm_hour
        minute = current_time.tm_min
        second = current_time.tm_sec

        secondMinute = round(second / 60, 5)
        secondHour = round(secondMinute / 60, 5)
        secondDay = round(secondHour / 24, 5)

        minuteHour = round(minute / 60, 5)
        minuteDay = round(minuteHour / 24, 5)

        hourDay = round(hour / 24, 5)

        timePassed += day + hourDay + minuteDay + secondDay
        break

resultTemp = round(timePassed/daysInTheYear, 5)

resultTemp = str(resultTemp)

digits = [str(digit) for digit in resultTemp]

if 'e' in digits:
    result = 'Wait 2 seconds'
elif len(digits) == 3:
    result = '100%'
elif int(digits[2]) == 0:
    corectList = digits.pop(0)
    corectList = digits.pop(0)
    corectList = digits.pop(0)
    temp = ''

    for i in digits:
        temp += i

    result = temp[:1] + '.' + temp[1:] + '%'
elif int(digits[2]) > 0:
    corectList = digits.pop(0)
    corectList = digits.pop(0)
    temp = ''

    for i in digits:
        temp += i

    result = temp[:2] + '.' + temp[2:] + '%'

print(result)