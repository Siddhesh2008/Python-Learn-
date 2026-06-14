#list=[] ordered and changeable . duplicates OK

fruits=["apple","orange","banana","kiwi"]
#print(dir(fruits))     #to display the attributes and methods
#print(help(fruits))    #gives the in depth description of the attributes
print(fruits)         #to access them fruits[]
print(fruits[::])       #to access them fruits[start:stop:step]
print(len(fruits))             # to find the length of the list
print("apple" in fruits)     #shows if it is present in the list
fruits[0] = "grape"  # to change an item
fruits.append("pineapple")  #to add an element to the end
fruits.remove("orange")    #to remove an element
fruits.insert(3,"pineapple") #to insert an element 
fruits.sort()               #to sort in alpha order
fruits.reverse()             #to reverse a list
#fruits.clear()               #clears a list.i am putting this as a comment
print(fruits.index("pineapple"))      #finds the index of the given value
print(fruits.count("pineapple"))    #finds the number of time a value is in the given list


for x in fruits:
    print(x)
