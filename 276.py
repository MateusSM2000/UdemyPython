import datetime
from dateutil.relativedelta import relativedelta

data_inicio = '27/02/1987 15:02:46'
data_fim = datetime.datetime.now()

data_inicio_formatado = datetime.datetime.strptime(data_inicio, '%d/%m/%Y %H:%M:%S')

print(data_inicio_formatado > data_fim)
print(data_inicio_formatado < data_fim)
print(data_inicio_formatado == data_fim)
print()

time_delta = data_fim - data_inicio_formatado
print(time_delta)
print()
print(time_delta.days)
print(time_delta.seconds)
print(time_delta.total_seconds())
print()

print(datetime.timedelta(weeks=1, days=10, hours=13, minutes=45, seconds=30))
print(data_fim + datetime.timedelta(weeks=1, days=10, hours=13, minutes=45, seconds=30))
print()

print(relativedelta(data_fim, data_inicio_formatado))
print(relativedelta(data_fim, data_inicio_formatado) + data_fim)