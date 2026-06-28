#*args      =allows you to pass multiple non-key arguments 
#**kwargs = allows you to pass mutiple keywords argument\
#            *unpacking operator
#          

def add(*nums):
    total=0
    for num in nums:
        total+= num
    return total

def print_address(**kwargs):
    for value in kwargs.values():
        print(value,end=" ")

print(add(1,2,3))
print_address(street="123 Main St", city="Anytown", state="CA", zip="12345")
