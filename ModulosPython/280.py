import calendar, locale

print(locale.getlocale())
locale.setlocale(locale.LC_ALL,'fr_FR')
#locale.setlocale(locale.LC_ALL,'')
print(locale.getlocale())

print(calendar.calendar(2025))