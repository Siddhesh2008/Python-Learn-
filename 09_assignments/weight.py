weight=float(input("Enter the weight: "))
unit=input("kilograms or pounds? (K or L): ")

if unit=="K":
    weight*=2.205
    unit="Lbs."
    print(f"the weight is:{round(weight,1)} {unit}")
elif unit=="L":
    weight/=2.205
    unit="Kgs."
    print(f"the weight is:{round(weight,1)} {unit}")
else:
    print(f"{unit} is invalid")



