import random

options = ['Rock', 'Paper', 'Scissors']

def game():

    while True:

        #choice = 0

        random_choice = random.choice(options)

        choice = input('Choose Rock, Paper or Scissors : ')

        print(f'Computer chose: {random_choice}')

        if choice == random_choice:
            print('It \'s a tie!')

        elif choice == 'Rock':
            if random_choice== "Scissors":
                print('You win!')
            else:
                print('You Lose!')

        elif choice == 'Paper':
            if random_choice == "Rock":
                print('You win!')
            else:
                print("You Lose!")

        elif choice == "Scissors":
            if random_choice == "Paper":
                print("You win!")
            else:
                print("You Lose!")

        else:
            raise ValueError(" Invalid Operation Selected!!! ")
        
        play_again = input('Do you wan to play again (y/n): ')

        if play_again == 'n':
            print('Thanks for playing!')
            break

game()

        

        



