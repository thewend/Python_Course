import random

highest = 10
answer = random.randint(1,highest)
print(answer) #TODO Remove after testing
guess = 99
while guess != answer:
    guess = int(input( "Please guess a number between 1 and {} ".format(highest)))
    if guess == answer:
        print('Congratulations, you guessed correctly.')
        break
    if guess == 0:
        print('Program stopped.')
        break
