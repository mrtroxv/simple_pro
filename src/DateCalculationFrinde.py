import datetime
time = datetime.datetime.now()
year = time.year
month = time.month
day = time.day


def calculate_day(my_date):
    birthdate = datetime.datetime.strptime(my_date, '%d/%m/%Y')
    birthdate = birthdate.replace(year=time.year)
    time_diffrent = birthdate-time
    if time_diffrent.days > 0:
        return time_diffrent.days
    elif time_diffrent.days == 0:
        return 0
    else:
        my_date_365=time_diffrent.days+365
        return my_date_365
