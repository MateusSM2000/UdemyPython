import calendar

print(calendar.calendar(2025))
print(calendar.month(2024,5))

print(calendar.monthrange(2025, 2))
print(list(calendar.day_name))
a = calendar.weekday(2025,2,calendar.monthrange(2025, 2)[1])
print(a)
print(list(calendar.day_name)[a])
print()

print(calendar.monthcalendar(2025,2))
week = 2
week_day = list(calendar.day_name).index('Thursday')
print(calendar.monthcalendar(2025,2)[week][week_day])