#! /usr/bin/env python3
# Determines if password string passed is 'strong'


import re, sys


def isStrong(password):
    passwordRegex = re.compile(r'''(?=.*?[A-Z]) # Checks for at least one uppercase
                                   (?=.*?[a-z]) # Checks for at least one uppercase
                                   (?=.*?[0-9]) # Checks for at least one digit
                                   [A-za-z\d]{8,}$''', re.VERBOSE)
    if passwordRegex.match(password):
        print('You have a strong password.')
    else:
        print('You have a weak password')


while True:
    password = input('Enter your password (Enter 0 to exit): ')
    if int(password) == 0:
        sys.exit()
    else:
        isStrong(password)
