#compound intrest calculator

principle=0
rate=0
time=0

while principle<=0:
    principle=float(input("Enter your principle amount: "))
    if principle<=0:
        print("principle cannot be less than zero")
    

while rate<=0:
    rate=float(input("Enter your intrest rate: "))
    if rate<=0:
        print("intrest rate cannot be less than zero")
    
while time<=0:
    time=int(input("Enter your time period: "))
    if time<=0:
        print("time cannot be less than zero")


total_amount=principle*pow((1+rate/100),time)
print(f"Balance after {time} year/s :{total_amount:,.2f} ")