#! /usr/bin/env python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard and capitalizes them

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):    # loops through all indexes in the "lines" list
    lines[i] = '* ' + lines[i]  # add a star to each string in "lines" list
text = '\n'.join(lines)
text = text.upper()

pyperclip.copy(text)
