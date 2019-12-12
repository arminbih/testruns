secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1 #guess count = guess count + 1 skraceno#
    if guess == secret_number:
        print ('Yout won! ')
        break
else:
    print ('Sorry you failed')

    