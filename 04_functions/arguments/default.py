#default arguments=A default value for certain paramaeters default is used when 
#                   that arguement is omitted ,make your functions more flexible, reduces num of arguments
#                   1. positional 2. DEFAULT 3. keyword 4. arbitrary

def net_price(list_price,discount=0,tax=0.05):     #discount and tax are default values now
    return list_price*(1-discount)*(1+tax)

print(net_price(500))