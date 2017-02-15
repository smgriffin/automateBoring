#! /usr/bin/env python3
# Python3 program which takes a list of strings and displays it in a table


def printTable(tableData):
    maxWidth = []
    for i in range(len(tableData)):
        maxWidth.append(max(len(s) for s in tableData[i]))
    # justWidth = max(maxWidth) - uncomment for equal length columns

    for j in range(len(tableData[0])):
        for k in range(len(tableData)):
            print(str(tableData[k][j]).rjust(maxWidth[k], ' '), end=" ") # Replace maxWidth with justWidth for equal sized columns
        print('\n')


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
