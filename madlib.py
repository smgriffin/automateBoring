#! /usr/bin/env python3
# Reads text files and let's user replace blanks with their own words.

import os, re

os.chdir('/users/sg/documents/automateboring')

madStory = open('madstory.txt')
text = madStory.read()
blank = re.findall(r"(NOUN|ADJECTIVE|VERB)", text)
print(blank)
madReplace = {words: '' for words in blank}
print(madReplace)
for i in madReplace.keys():
    madReplace[i] = input('Please enter a %s: ' % 'word')

with open('madstory.txt') as infile, open('madfinal.txt', 'w') as outfile:
    for line in infile:
        for k, v in madReplace.items():
            line = line.replace(k, v)
infile.close()
outfile.close()
