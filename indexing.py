#[start:end:step]

credit_number="1234-5678-9812-3456"

print(credit_number[0:4]) #1234
print(credit_number[5:9]) #5678
print(credit_number[10:14]) #9812
print(credit_number[15:19]) #3456
#or
print(credit_number[:4]) #1234 both are same
print(credit_number[5:]) #5678-9812-3456 
print(credit_number[-1]) #6

print(credit_number[::3]) #counts every third charcter
print(f"XXXX-XXXX-XXXX-{credit_number[-4:]}") #masking the credit card number except last 4 digits
print(credit_number[::-1]) #reversing the string
