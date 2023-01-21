day_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
def day_of_year(day,month,year):
    day_of_years = 0
    if is_leap(year):
        day_in_month[2] += 1
    else:
        if month == 2  and day == 29:
            return -1
    for i in range(1,month):
        day_of_years += day_in_month[i]
    day_of_years += day
    return day_of_years
def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
def date_diff(date1,date2):
    date1 = [int (e) for e in date1.split("-")]
    date2 = [int (e) for e in date2.split("-")]  
    sum_1 = day_of_year(date1[0],date1[1],date1[2])
    sum_2 = day_of_year(date2[0],date2[1],date2[2])
    date_diffs = 0
    for year in range(date1[2],date2[2]):
        date_diffs += day_in_year(year)
    return ((sum_2 - sum_1 + date_diffs) + 1)
def day_in_year(year):
    if is_leap(year):
        return 366
    else:
        return 365


