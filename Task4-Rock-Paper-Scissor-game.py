import random

rock = '''
 ___'-------
        ----)
       (-----)
       (-----)
       (----)
 ---,_-(---)
'''

paper = '''
     -------
 ---'    ----)----
          ------)
         --------)
         --------)
 ___'----------)
'''

scissors = '''
     -------
---'   ----)---
          ------)
      ----------)
        (----)
___'---(---)
'''

game_images = [rock, paper, scissors]

user_score = 0
computer_score = 0
play_again = 'yes'

while play_again.lower() in ['yes', 'y']:
    user_choice = int(input("Enter your choice: Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
    if user_choice >= 3 or user_choice < 0:
        print("You entered an invalid number. You lose.")
        computer_score += 1
    else:
        print("Your choice:", user_choice)
        print(game_images[user_choice])

        computer_choice = random.randint(0, 2)
        print("Computer's choice:", computer_choice)
        print(game_images[computer_choice])

        if computer_choice == user_choice:
            print("It's a tie!")
        elif (computer_choice == 0 and user_choice == 2) or (computer_choice == 1 and user_choice == 0) or (computer_choice == 2 and user_choice == 1):
            print("You lose!")
            computer_score += 1
        else:
            print("You win!")
            user_score += 1

    print(f"Score - You: {user_score} | Computer: {computer_score}")
    
    while True:
        play_again = input("Do you want to play again? (yes or no): ").lower()
        if play_again in ['yes', 'y', 'no', 'n']:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


print("Thanks for playing! Goodbye!")
