from datetime import date, time, datetime

d1 = date.today()
# print(d1)

t1 = time(6, 30, 00)
# print(t1)

dt1 = datetime.now()
print(dt1)

print(d1.day)
print(d1.year)

print(t1.hour)

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print(dt1.month)
print(dt1.weekday())

print(days[dt1.weekday()])

d1 = d1.replace(year=2020, month=6, day=24)
t1 = t1.replace(hour=12)
dt1 = dt1.replace(year=2031, month=7)
print(d1)
print(t1)
print(dt1)

now = datetime.now()

print(now)
# Days
print(now.strftime("%a, %A, %w, %d"))
# Months
print(now.strftime("%b, %B, %m"))
# Time
print(now.strftime("%H, %I, %M, %S, %p"))
# Local time
print(now.strftime("%c"))
print(now.strftime("%X"))

dt1 = datetime(2022, 6, 1, 12)
dt2 = datetime(2022, 1, 6, 12)

# print(dt1>dt2)
# print(dt1<dt2)

# delta = dt1 - dt2
# print(delta)
# print(delta.days)
# print(delta.seconds)

from datetime import timedelta

now = datetime.now()
one_month = timedelta(days=30)
one_week = timedelta(weeks=1)

print("One month+ :", now + one_month)
print("One week+ :", now + one_week)
print("One week- :", now - one_week)