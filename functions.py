#function=reusable block of code
def example(num):
    print(f'example {num}')
    print("this is an example")
    print(f"example {num}")
    print()

example("15")

#return=statement used to end a function and send the result back to the caller

def add(x,y):
    z=x+y
    return z

def subtract(x,y):
    z=x-y
    return z

print(add(1,2))
print(subtract(7,6))
