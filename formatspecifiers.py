price1=3000.1456
price2=-9870.65
price3=1200.34

print(f"price 1 is ${price1:.1f}")   #for decimal 
print(f"price 2 is ${price2:.1f}")
print(f"price 3 is ${price3:.1f}")
print(" ")
print(f"price 1 is ${price1:10}")   ##for space
print(f"price 2 is ${price2:10}")
print(f"price 3 is ${price3:10}")
print(" ")
print(f"price 1 is ${price1:<10}")   ##for left justify and vice-versa
print(f"price 2 is ${price2:<10}")
print(f"price 3 is ${price3:<10}")
print(" ")
print(f"price 1 is ${price1:+}")   #for signs
print(f"price 2 is ${price2:+}")
print(f"price 3 is ${price3:+}")
print(" ")
print(f"price 1 is ${price1:,}")   #for thousand separating
print(f"price 2 is ${price2:,}")
print(f"price 3 is ${price3:,}")
print(" ")
print(f"price 1 is ${price1:+,.2f}")   #combinations
print(f"price 2 is ${price2:+,.2f}")
print(f"price 3 is ${price3:+,.2f}")