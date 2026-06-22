#Magic methods=dunder methods __init__,__str__,__eq__ .
#they are automatcally called by many of pyhton's built-in operations.
#they allow developers to define or customize the behavior of  objects

class Book:

    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages

    def __str__(self):
        return f"{self.title} by {self.author}"      #to prevent printing the memory location
    def __eq__(self,other):
        return self.title==other.title and self.author==other.author    #to check equality
    def __lt__(self, other):
        return self.pages<other.pages             #to check less than
    def __gt__(self, other):
        return self.pages<other.pages              #to check greater than
    def __add__(self, other):
        return self.pages+other.pages             #to add pages
    def __contains__(self,keyword):
        return keyword in self.title or keyword in self.author     #to check if keyword is in title or author
    def __getitem__(self,key):
        if key=="author":
            return self.author
        elif key=="title":
            return self.title
        else:
            return "Invalid key"
          
book1=Book("The Alchemist","Paulo Coelho",208)
book2=Book("Harry Potter","j.k Rowling",206)
book3=Book("qwerty","asdfg",206)

print(book1)
print(book1==book2)
print(book1<book2)
print(book1.pages+book2.pages)
print("Rowling" in book1)
print(book1["author"])