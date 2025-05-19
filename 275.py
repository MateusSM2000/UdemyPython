import datetime, pytz

data = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
print(data)

print(data.timestamp())  #mostra quantos segundos se passaram desde o marco zero do unix time stamp
print(datetime.datetime.fromtimestamp(data.timestamp()))