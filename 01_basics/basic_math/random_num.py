import random 
low=1
high=100
options=("rock","paper","scissors")
cards=["2","3","4","5","6","7","8","9","A"]

number=random.randint(low,high)
fnumber=random.random()      #for a random float number from0-1
option=random.choice(options)       #picks a random element
random.shuffle(cards)      #shuffles a given list
print(number)
print(fnumber)
print(option)
print(cards)