unit=input("Is this temprature in Celsius or Farenheit (C/F): ")
temp=float(input("Enter the tempraure: "))

if unit=="C":
    temp=round((9*temp)/5 +32,1)
    print(f"The temprautre in farenheit is: {temp}F")
elif unit=="F":
    temp=round((temp-32)*5/9,1)
    print(f"The temprautre in Celsius is: {temp}C")
else:
    print(f"{unit} is an invalid measurement")