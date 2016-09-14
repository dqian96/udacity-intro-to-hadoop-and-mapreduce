#!/usr/bin/python

# Reducer for (Sale, Sales) KVPS
# Find the number of sales and the total amount of sales
# Reduce("sale", [1,2,3,...,4]) -> [20, 3232323]

import sys

DELIMITER = '\t'

def parseLine(line):
	data = line.strip("\n").split(DELIMITER)
	if len(data) != 2:
		return () 
	return (data[0], float(data[1]))

def emit(key, value):
	output = ""
	for i in range(0, len(value)):
		output += str(value[i])
		if i != len(value) - 1:
			output += DELIMITER
	print key + DELIMITER + output


totalSales = 0
amountOfSales = 0

for line in sys.stdin:
	data = parseLine(line)
	if len(data) == 0:
		continue

	newValue = data[1]
	totalSales += 1
	amountOfSales += newValue

if totalSales != 0:
	emit("Sales", [totalSales, amountOfSales])
