#!/usr/bin/python

import sys

DELIMITER = '\t'

def parseLine(line):
    return line.strip("\n").split(DELIMITER)

def emit(key, value):
    print(key + DELIMITER + value)

# Reduce("word", [nodes]) -> [unique_nodes])
def reducer():
    currDay = None
    numPurchases = 0
    revenue = 0
    for line in sys.stdin:
        data = parseLine(line)
        # change days
        if currDay and currDay != data[0]:
            if numPurchases == 0:
                meanPurchase = 0
            else:
                meanPurchase = revenue/numPurchases
            emit(currDay, str(meanPurchase))
            currDay = data[0]
            numPurchases = 0
            revenue = 0
        # same word
        if currDay is None or currDay == data[0]:
            currDay = data[0]
            revenue += float(data[1])
            numPurchases += 1
    
    if currDay:
        if numPurchases == 0:
            meanPurchase = 0
        else:
            meanPurchase = revenue/numPurchases
        emit(currDay, str(meanPurchase))

def main():
    reducer()

if __name__ == "__main__":
    main()