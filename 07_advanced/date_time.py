import datetime
date=datetime.date(2026,1,20)
today=datetime.date.today()

time=datetime.time(12,34,56)
dt=datetime.datetime(2026,1,20,12,34,56)
now=datetime.datetime.now()

fnow=now.strftime("%B %d,%Y %H:%M:%S")

target_datetime= datetime.datetime(2030,1,20,12,34,56)

if target_datetime>now:
    print("The target datetime is in the future")
else:
    print("The target datetime is in the past")

print(date)
print(today)
print(time)
print(datetime)
print(now)