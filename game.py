# paper wins from rock
# rock wins from scissor
# scissor wins from paper
# 1 = rock
# 2 = paper
# 3 = scissor
# step take user input
# step 2 convert  user input
# step 3 generate value from computer
# step 4 compare both values
# step 5 print result

import random


def user_choice():
    user_choice = input('ENTER YOUR CHOICE : ')

    for x, y in choices_dict.items():
        if user_choice.lower() == x.lower():
            choice = y
            return choice


print('_______ROCK PAPER SCISSOR_______')
print('WINNING RULES FOR THE GAME')
print('Rock vs Paper -> Paper Wins')
print('Rock vs Scissor -> Rock Wins')
print('Scissor vs Paper -> Scissor Wins')
counter = 1
while True:
    print('CHOICES ->  \n 1-> Rock \n 2-> Paper \n 3-> Scissor')
    choices_dict = {
        'Rock': 1,
        'Paper': 2,
        'Scissor': 3
    }
    choice = user_choice()
    com_choice = random.randint(1, 3)
    for x, y in choices_dict.items():
        if com_choice == y:
            print('NOW ITS COMPUTER TURN .......')
            print('COM CHOICE IS : ', x)
    counter += 1
    if choice == com_choice:
        print('IT IS A TIE')
    elif choice == 1 and com_choice == 2:
        print('Paper WINS')
    elif choice == 1 and com_choice == 3:
        print('ROCK WINS', )
    elif choice == 2 and com_choice == 1:
        print('Paper WINS')
    elif choice == 2 and com_choice == 3:
        print('SCISSOR WINS')
    elif choice == 3 and com_choice == 1:
        print('ROCK WINS')
    elif choice == 3 and com_choice == 2:
        print('SCISSOR WINS')

    if counter == 4:

        ans = input('Do you wanna to play again ? '
                    '(Y / N) : ').lower()
        if ans == "n":
            break
        elif ans == 'y':
            counter = 0
        else:
            print('invalid choice')
        if counter == 4:
            break
        counter += 1






