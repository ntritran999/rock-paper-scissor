from random import randint


def invalid_move():
    if human_choice!="rock" and human_choice!="paper" and human_choice!="scissor": return True

def win():
    if human_choice=="rock"     and computer_choice=="scissor":   return True
    if human_choice=="paper"    and computer_choice=="rock":      return True
    if human_choice=="scissor"  and computer_choice=="paper":     return True

def lose():
    if human_choice=="rock"     and computer_choice=="paper":     return True
    if human_choice=="paper"    and computer_choice=="scissor":   return True
    if human_choice=="scissor"  and computer_choice=="rock":      return True

def draw():
    if human_choice==computer_choice:                             return True

def play_again():
    global run
    play_again = input("Do you want to play again? [y]/[n]: ") 
    if play_again == "n": 
       print("Thanks for playing!") 
       run = False
# Main loop
run = True
while run: 
    i = randint(1, 3)
    computer_choice = ""
    human_choice = input("Choose 'rock', 'paper' or 'scissor': ")
    if i == 1: computer_choice += "rock"
    if i == 2: computer_choice += "paper"
    if i == 3: computer_choice += "scissor"
    
    if invalid_move(): 
        print("Invalid move!")

    else:
        print(f"You chose: {human_choice}")
        print(f"Computer chose: {computer_choice}")
        

    if win():
        print("YOU WON!")
        play_again()
    if lose():
        print("YOU LOST!")
        play_again()     
    if draw():
        print("It's a draw!")
        play_again()
