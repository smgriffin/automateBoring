# Converts list to comma separated string with 'and' before final item
spamList = []   # create empty list
while True:    # Filling list with user input
    print('Enter the items in the list to be format ' +
          '(Or enter nothing to stop.)')
    spam = input()
    if spam == '':
        break
    spamList = spamList + [spam]


def comma(commaList):   # function changes list to formatted str
    for i in range(len(commaList)):
        if i < len(commaList) - 2:
            print(str(commaList[i]) + ', ', end="")
        else:
            print(str(commaList[len(commaList) - 2]) + ' and ', end="")
            print(str(commaList[len(commaList) - 1]))
            break


comma(spamList)     # call function
