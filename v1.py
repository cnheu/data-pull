__author__ = 'christophernheu'

import csv

with open('test1.csv', mode='r') as infile:
    reader = csv.reader(infile, delimiter=';')



    # array = [[ColA],[ColB],[ColC],...,]
    colVal = []
    rowVal

    for line in infile:
        rowNum = 0

        for colNum in range (0,13):
            colVal[colNum] = line[colNum]
            rowVal[rowNum] = line[colNum]


        rowNum += 1

    print(array)





