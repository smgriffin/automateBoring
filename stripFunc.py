#! /usr/bin/env python3
# Using regex to take string and do same thing as strip() function

import re


def stripTool(stripString, stripSide):
    regexStripLeft = re.compile(r'^\s+')  # matches left side whitespace
    regexStripRight = re.compile(r'\s*$')  # matches right side whitespace
    if stripSide == 'Left':
        print(regexStripLeft.sub('', stripString))
    elif stripSide == 'Right':
        print(regexStripRight.sub('', stripString))
    else:
        newString = regexStripLeft.sub('', stripString)
        finalString = regexStripRight.sub('', newString)
        print(finalString)


stripString = input('Please enter your string to be formatted: ')
stripSide = input(r'''Please enter Left or Right to choose which side to strip (enter anything else for full strip):''')
stripTool(stripString, stripSide)
