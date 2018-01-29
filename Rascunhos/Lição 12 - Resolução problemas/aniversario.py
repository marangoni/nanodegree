# Given your birthday and the current date, calculate your age
# in days. Compensate for leap days. Assume that the birthday
# and current date are correct dates (and no time travel).
# Simply put, if you were born 1 Jan 2012 and todays date is
# 2 Jan 2012 you are 1 day old.

# IMPORTANT: You don't need to solve the problem yet!
# Just brainstorm ways you might approach it!

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    ##
    # Your code here. Return True or False
    # Pseudo code for this algorithm is found at
    # http://en.wikipedia.org/wiki/Leap_year#Algorithm
    ##

    if year % 4 <> 0:
        return False
    elif year % 100 <> 0:
        return True
    elif year % 400 <> 0:
        return False
    else:
        return True

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    ##
    days = 0
    sum_year = 0
    sum_month = 0

    for y in range(y1,y2):
        if isLeapYear(y):
            sum_year = sum_year + 364
        else:
            sum_year = sum_year + 365

    if m2 > m1:
        for m in range(m1,m2):
            sum_month = sum_month + daysOfMonths[m]
    else:
        for m in range(m2,m1):
            sum_month = sum_month + daysOfMonths[m]

    if d2 > d1:
        sum_days = d2 - d1
    else:
        sum_days = d1 - d2

    days = sum_year + sum_month + sum_days
    ##
    return days


print 'Parabens voce tem ' + str(daysBetweenDates(2000,02,01,2000,03,01)) + ' dias de vida'
