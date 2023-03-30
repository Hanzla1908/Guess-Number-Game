# import random librery
import random
# give a range
random_number = random.randint(1, 10)
# add counter verriable for count the attempts
counter = 1
# get input from the user
guess_number = int(input('guess the number in range (1,10) '))
# applying loop for reapetition
while guess_number != random_number:
    # appling the conditions
    if guess_number < random_number:
        print('Wrong! The number is heigher')
    else:
        print('Wrong!The number is lower')
    guess_number = int(input('guess the number again '))
    counter += 1
else:
    # print if the guess is correct
    print("You'r guess is Correct! Number is", guess_number, end=' , ')
    print('But in', counter, 'Attempts')
