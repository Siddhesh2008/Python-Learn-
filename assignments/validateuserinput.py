#1.username is no more than 12 characters
#2.username must not contain spaces
#3.username must not contain digits

username=input("Enter A Username: ")

if len(username)>12:
    print("Your Username cannot be more than 12 characters")
elif not username.find(" ")==-1:
    print("Your Username cannot contain spaces")
elif not username.isalpha():
    print("Your Username cannot contain digits")
else:
    print(f"Welcome!! {username.capitalize()}")
