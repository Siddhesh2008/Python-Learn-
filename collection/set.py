#set={} unordered and immutable, but add/remove OK. NO duplicates

fruits={"apple","orange","banana","coconut"}
print(len(fruits))
print("pineapple" in fruits)

#print(fruits[])         #error 
fruits.add("pineapple")
fruits.remove("apple")
fruits.pop()       #removes randomly
#fruits.clear()       #clears
