temp=25              ##for OR operator example
is_raining=False

if temp>35 or temp<0 or is_raining:
    print("the outdoor event is cancelled ")
else:
    print("the outdoor event is still scheduled")

temp=25               ## for and operator example
is_sunny=True

if temp>=28 and is_sunny:
    print("it is hot outside")
    print("it is sunny")
elif temp<=0 and is_sunny:
    print("it is cold outside")
    print("it is sunny")
elif 28>temp>0 and  is_sunny:
    print("it is mild outside")
    print("it is sunny")
if temp>=28 and not is_sunny:         ##NOT operator example
    print("it is hot outside")
    print("it is cloudy")
elif temp<=0 and not is_sunny:
    print("it is cold outside")
    print("it is cloudy")
elif 28>temp>0 and not is_sunny:
    print("it is mild outside")
    print("it is cloudy")


