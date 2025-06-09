import datetime

data = datetime.datetime(2024,2, 5)
print(data)

data2 = datetime.datetime(2024,2,6,13,29,8)
print(data2)

data3 = datetime.datetime(2024,2,6,13,29,8,695146)
print(data3)

data4 = datetime.datetime.strptime('26-02-2025 15:55:30', '%d-%m-%Y %H:%M:%S')
print(data4)

