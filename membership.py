#Membership operators= in, not in
#Membership operators are used to test if a value is present in a sequence (like a string)

word="APPLE"

letter=input("Guess a letter: ").upper()

if letter in word:
    print(f"Correct! {letter} is in the word.")

else:
    print(f"Incorrect! {letter} is not in the word.")