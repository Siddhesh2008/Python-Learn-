#tuple=() ordered and unchangeable .Duplicates OK

fruits=("apple","orange","banana","coconut","coconut")
print(len(fruits))
print("pineapple" in fruits)

print(fruits.index("apple"))
print(fruits.count("coconut"))

for fruit in fruits:
    print(fruit)

