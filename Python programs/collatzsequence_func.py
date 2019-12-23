def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1

choosenint = int(input('Enter an integer greater then 1: '))
print (choosenint)
while choosenint != 1:
    choosenint = collatz(choosenint)
    print (choosenint)