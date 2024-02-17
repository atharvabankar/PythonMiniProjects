print("Welcome to the Quiz game")
playing=input("Do you want to Start? ").lower()
score=0

if playing != "yes":
  quit()

print("okey Lets starts :)")

answer=input("What is full form of cpu? \n").lower()
if answer == "central processing unit":
  print("Correct")
  score +=1
else:
  print("Wrong anser")
  print("Your score is:",score)
  quit()

answer=input("What is full form of py? \n").lower()
if answer=="python":
  print("Correct")
  score +=1
else:
  print("wrong")
  print("Your score is:",score)
  quit()

answer=input("What is full form of gpu? \n").lower()
if answer=="graphic processing unit":
  print("Correct")
  score +=1
else:
  print("wrong")
  print("Your score is:",score)
  quit()

answer=input("What is full form of ram? \n").lower()
if answer=="random access memory":
  print("Correct")
  score +=1
else:
  print("wrong")
  print("Your score is:",score)
  quit()

print("Your score is:",score)
print("you got",(score/4)*100,"% of questions correct")