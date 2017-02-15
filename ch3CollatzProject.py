def collatz(number):
    if number % 2 == 0:
        x = number / 2
    elif number % 2 == 1:
        x = 3 * number + 1
    return int(x)


try:
    y = int(input('Please enter a number: '))
except ValueError:
    print('You must enter an integer')

if y == 1:
    print(y)
else:
    while y != 1:
        y = collatz(y)
        print(str(y))
