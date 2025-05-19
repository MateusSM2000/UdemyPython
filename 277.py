import datetime

print(datetime.datetime.strftime(datetime.datetime.now(), '%d/%m/%Y'))
print(datetime.datetime.strftime(datetime.datetime.now(), '%d/%m/%Y %H:%M'))
print(datetime.datetime.strftime(datetime.datetime.now(), '%Y'))
print(isinstance(datetime.datetime.strftime(datetime.datetime.now(), '%Y'), str))
print()

data = datetime.datetime.now()
print(data.year)
print(isinstance(data.year, int))
