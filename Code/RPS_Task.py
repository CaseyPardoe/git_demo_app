import random

def get_user_choice():
    user_choice = input("Please choose between Rock, Paper or scissors: ").lower()
    while user_choice not in {'rock', 'paper', 'scissors'}:
          print("Invalid choice. Please enter rock, paper, or scissors.")
          user_choice = input("Please input valid choice: ").lower()
    return user_choice

def get_computer_choice():
     return random.choice(['rock', 'paper', 'scissors'])

def who_wins(user_choice, computer_choice):
     if user_choice == computer_choice:
        return "Its a tie!"
     elif(
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper')
     ):
          return 'You Win!'
     else:
          return 'Your a loser!'
     
rounds_played = 0
user_wins = 0
computer_wins = 0

while True:
     print(f"Round {rounds_played +1}")

     user_choice = get_user_choice()
     computer_choice = get_computer_choice()

     print(f"Computer chose {computer_choice}")
     result = who_wins(user_choice, computer_choice)
     print(result)

     if 'Win' in result:
          user_wins += 1
     elif 'tie' not in result:
          computer_wins += 1

     rounds_played +=1

     print(f"""
     Results so far:
     Rounds Played: {rounds_played}
     Player Wins: {user_wins}
     Computer Wins: {computer_wins}
     """)

     replay = input('Do you want to play again? (Yes or No)')
     if replay not in ('yes', 'y'):
        print("Thanks for playing! Goodbye!")
        break



    

    
    
          
    