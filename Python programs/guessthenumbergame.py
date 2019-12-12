import random
secret_number = random.randint (1, 9)
print ('I am thinking of a number between 1 and 9' )

for guesses_taken in range (1, 4):
    guess = (int(input('Take a guess: ')))
    
    if guess < secret_number:
        print ('Guess too low')
    elif guess > secret_number:
        print ('Guess too high')
    else:
        break

if guess == secret_number:
    print (f"Good job you guessd my number in {str(guesses_taken)} attempts ")
else:
    print (f"Nope the correct number is {str(secret_number)} ")