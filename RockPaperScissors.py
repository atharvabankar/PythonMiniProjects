import random

options = ["rock", "paper", "scissor"]
user_wins = 0
comp_wins = 0

while True:
  user_choice = input("Enter rock,paper,scissor or q to quit: ").lower()
  if user_choice == "q" not in options:
    break

  if user_choice not in options:
    continue

  random_number = random.randint(0, 2)
  computer_pick = options[random_number]
  print("computer picked", computer_pick, ".")

  if user_choice == "rock" and computer_pick == "scissor":
    print("You won!")
    user_wins += 1
  elif user_choice == "paper" and computer_pick == "rock":
    print("You won!")
    user_wins += 1
  elif user_choice == "scissor" and computer_pick == "paper":
    print("You won!")
    user_wins += 1
  elif user_choice == computer_pick:
    print("Draw")
  else:
    print("Computer wins")
    comp_wins += 1

print("you wins", user_wins, "times")
print("computer wins", comp_wins, "times")
print("Goodbye")
