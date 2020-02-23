import random

sec_num = random.randint(1,20)
print('I have a number in mind between 1 and 20')

for guess_taken in range(1,7):
    print('Enter your guess: ')
    guess = int(input())

    if guess < sec_num:
        print('Your guess is too low')
    elif guess > sec_num:
        print('Your guess is too high')
    else:
        break

if (guess == sec_num):
    print('Congrats! You guessed the correct number in ' + str(guess_taken) + ' attempts.')
else:
    print('Sorry, you were not able to guess the correct number, the number was: ' + str(sec_num))  