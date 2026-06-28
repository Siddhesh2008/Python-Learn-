#Decorator = A function that extends the behaviour another function w/0 modifying the base function
#pass the base function as an argument to the decorator


def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("*You get sprinkles*")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("*You get fudge*")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(Flavor):
    print(f"You get {Flavor} ice cream")

get_ice_cream("cxhocolate")