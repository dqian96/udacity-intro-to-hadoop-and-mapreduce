#!/usr/bin/python

from datetime import datetime
import sys

DELIMITER = '\t'

# parse a transaction
def parseTransaction(log):
    transactionData = log.split(DELIMITER)
    weekday = datetime.strptime(transactionData[0], "%Y-%m-%d").weekday()
    transactionData.append(weekday)
    return transactionData

def emit(key, value):
    print(key + DELIMITER + value)

# mapper 
# Map(transactionLogChunk, "2016-0...") -> [("Monday, 23"), ("Tuesday", "32"),...]
def mapper():
    for transaction in sys.stdin:
        transactionData = parseTransaction(transaction)
        day = str(transactionData[-1])
        expenditure = transactionData[4]
        emit(day, expenditure)

def main():
    mapper()

if __name__ == "__main__":
    main()