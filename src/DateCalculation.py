import datetime
time = datetime.datetime.now()
year = time.year
month = time.month
day = time.day


def calculate_day(my_date):
    birthdate=datetime.datetime.strptime(my_date,'%d/%m/%Y')
    birthdate=birthdate.replace(year=time.year)
    time_diffrent=birthdate-time 
    if time_diffrent.days>0:
        more_than_today(time_diffrent.days)
    elif time_diffrent.days==0:
        print("happy birthday today born a legend like u")
    else:
        less_than_today(time_diffrent.days)


def more_than_today(my_date):
    print(my_date)


def less_than_today(my_date):
    print(my_date+365)
