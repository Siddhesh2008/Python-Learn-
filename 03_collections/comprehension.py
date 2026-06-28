#List comprehension= A concise way to create lists in Python. 
# It allows you to generate a new list by applying an expression to each
#  item in an existing iterable (like a list, tuple, or string) and optionally 
# filtering the items based on a condition.

#doubles=[]
#for x in range(10):             #old method of creating a list using a for loop
 #   doubles.append(x*2)

# Using list comprehension
doubles = [x * 2 for x in range(10)]  # This creates a list of doubles from 0 to 18
print(doubles)  # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

tripled = [x * 3 for x in range(10)]  # This creates a list of triples from 0 to 27
print(tripled)  # Output: [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

squared = [x ** 2 for x in range(10)]  # This creates a list of squares from 0 to 81
print(squared)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# Using list comprehension to filter fruits that contain the letter 'a'

fruits_with_a = [fruit for fruit in fruits if 'a' in fruit]   #condition
print(fruits_with_a)  # Output: ['apple', 'banana', 'date']