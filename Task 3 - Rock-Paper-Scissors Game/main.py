#Rock-Paper-Scissor Game Project
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
import os

game_is_on = True
score = 0 
print("\nWELCOME TO ROCK-PAPER-SCISSOR GAME !!!\n")
while (game_is_on == True):
  print("0 for Rock || 1 for Paper || 2 for Scissors.\n")
  choose = int(input("What do you choose?: "))

  if (choose == 0):
    print(rock)
  elif (choose == 1):
    print(paper)
  elif (choose == 2):
    print(scissors)
  else:
    print("Invalid Input!")

  computer_choice = random.randint(0, 2)
  print(f"\nComputer chose {computer_choice}")

  if (computer_choice == 0):
    print(rock)
  elif (computer_choice == 1):
    print(paper)
  elif (computer_choice == 2):
    print(scissors)
  else:
    print("Invalid Input")

  if ((choose == 0) and (computer_choice == 0)):
    print("It's a Draw! Score: ",score)
  elif ((choose == 0) and (computer_choice == 1)):
    print("Computer Wins! Score: ",score)
  elif ((choose == 0) and (computer_choice == 2)):
    score += 1
    print("You Won! Score: ",score)

  if ((choose == 1) and (computer_choice == 0)):
    score += 1
    print("You Won! Score: ",score)
  elif ((choose == 1) and (computer_choice == 1)):
    print("It's a Draw! Score: ",score)
  elif ((choose == 1) and (computer_choice == 2)):
    print("Computer Wins! Score: ",score)

  if ((choose == 2) and (computer_choice == 0)):
    print("Computer Wins! Score: ",score)
  elif ((choose == 2) and (computer_choice == 1)):
    score += 1
    print("You Won! Score: ",score)
  elif ((choose == 2) and (computer_choice == 2)):
    print("It's a Draw! Score: ",score)
    
  print("\nDo you want to play again?: ")
  play_again = int(input("Press 1 for Yes || Press 0 for No\n-->"))
  if(play_again == 1):
    game_is_on = True
    os.system('cls') 
  elif(play_again == 0):
    game_is_on = False