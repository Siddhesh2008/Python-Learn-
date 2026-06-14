#quiz game

questions=("at what distance is the moon from the earth?",
"Which the biggest black hole in the Milky Way Galaxy?",
"What does STEM mean?",
"Which is the largest mountain in the world?",
"Which anime sigma ayanokoji comes in?",
"Is this quiz tuff?")


options=(("A.1 light year","B.2 light year","C.3 light year","D.4 light year"),
("A.puh","B.phoenix A","C.sagitarius","D.Ton 618"),
("A.science technology engineering maths","B.screen environment time management","C.idk","D.none of the above"),
("A.everest","B.fuji","C.mt.Massive","D.none of the above"),
("A.NARUTO","B.One piece","C.COTE","D.dragon ball"),
("A.YAHH","B.HELL YEAHH","C.YES","D.NO"))

answers=("A","C","A","A","C","B")
guesses=[]
score=0
question_num=0

for question in questions:
    print("------------------------------------------------")
    print(question)
    
    for option in options[question_num]:
         print(option)
            

            

       

    guess=input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        score+=1
        print("CORRECT!!")
    else:
        print("INCORRECT!!")
        print(f"{answers[question_num]} is the correct answer")
    question_num+=1

print("----------------------------")
print("         RESULTS        ")
print()
print("answers:",end=" ")
for answer in answers:
    print(answer,end=" ")
print()

print("guesses: ",end=" ")
for guess in guesses:
    print(guess,end=" ")
print()

score=int(score/len(questions)*100)
print(f"your score is {score}%")

print("______________________")
print("You Da REAL TOPPER!!!!")
