import random

top_of_range=input("Enter a number: ")
if top_of_range.isdigit():
  top_of_range=int(top_of_range)
else:
  print("Please enter a number next time:")
  quit()

random_number=random.randint(0,top_of_range)
gusses=0
while True:
  gusses+=1
  user_gusses=input("Make a Gusses: ")
  if user_gusses.isdigit():
    user_gusses=int(user_gusses)
  else:
    print("Enter the number next time:")
    continue

  if user_gusses == random_number:
    print("You got it!")
    break
  elif user_gusses < random_number:
    print("Your number is below ")
  else:
    print("your number is higher")

print("you goi in",gusses,"gusses")