#asking user to give input for two exam scores
score1=input("enter your score1 marks:")
score2=input("enter your score2 marks:")
#converting string into integer form
score1=int(score1)
score2=int(score2)
#giving conditions for the scores
if score1>=50 and score2>=50:
    print("You passed!")
else:
    print("You need to retake some exams")
