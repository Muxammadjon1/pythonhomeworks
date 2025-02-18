import random

while True:
    number = random.randint(1, 100)
    attempts = 10

    print("Guess the number (between 1 and 100). You have 10 attempts.")

    for i in range(attempts):
        num = int(input("Please enter the number: "))
        
            
        if num > number:
            print('Too high!')
        elif num < number:
            print("Too low!")
        else:
            print("You found it!")
            break 
    else:
        print('You did not find the number. Want to play again? (Y/YES/y/yes/ok) ')
        again = input().lower()
        if again not in ['y', 'yes', 'ok']:
            break  
   
