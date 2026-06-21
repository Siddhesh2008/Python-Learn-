#iterables= an object capable of returning its members one at a time. Examples include all sequence types (such as list, str, and tuple) and some non-sequence types like dict, file objects, and objects of any classes you define with an __iter__() or __getitem__() method.
#allow us to iterate over the elements of a collection, regardless of its specific type. This means we can use a for loop to traverse through lists, strings, tuples, dictionaries, and even custom objects that implement the iterable protocol.

numbers=[1, 2, 3, 4, 5]     
tuples=(1, 2, 3, 4, 5)      #tuples also work with iterables

for num in reversed(numbers):
    print(num)

fruits={"apple", "banana", "cherry"}     #sets also work with iterables

for fruit in fruits:     #but sets cannot be reversed because they are unordered collections, so we cannot guarantee the order of elements when iterating over them. Therefore, we cannot use the reversed() function with sets.
    print(fruit)

name="John Doe"     #strings also work with iterables

for char in name:
    print(char,end=" ")

my_dict={"name": "John", "age": 30, "city": "New York"}     #dictionaries also work with iterables

for key,value in my_dict.items():
    print(key, value)