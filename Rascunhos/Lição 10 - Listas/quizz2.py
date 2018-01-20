def how_many_days(mes):
#lista com os dias dos meses
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]
    return days_in_month[mes-1]

print how_many_days(3)
print how_many_days(1)
print how_many_days(2)
print how_many_days(12)
