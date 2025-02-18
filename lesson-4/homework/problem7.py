import random

computer_score=0
people_score=0
choices=['paper','rock','scissors']

print('Welcome to our game, Let\' start our game:')

while people_score<=5 and computer_score<=5:
    computer_choice=random.choice(choices)
    people_choice=input("Please enter your option:")
    if people_choice not in choices:
        print("Invalid choice")
        continue

    print(computer_choice)


    if people_choice==computer_choice:
        print("It is draw")
    elif (people_choice=='scissors' and computer_choice=='paper') or (people_choice=='rock' and computer_choice=='scissors') or (people_choice=='paper' and computer_choice=='rock'):
        print("You win this round, congratulations")
        people_score+=1
        print(f"Score-You: {people_score}, Computer:{computer_score}")
    else:
        print("Computer win in this game")
        computer_score+=1
        
        print(f"Score-You: {people_score}, Computer:{computer_score}")

    if people_score==5:
        print("Congratulations you win in this game")
    elif computer_score==5:
        print('Maybe next time')
