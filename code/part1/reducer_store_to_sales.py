#!/usr/bin/python

# Reducer for (Store, Sale) KVPS
# Find the largest sale in the list of sales.
# Reduce("Sbux", [1,2,3,...,4]) -> 2328

import sys

DELIMITER = '\t'

def parseLine(line):
	data = line.strip("\n").split(DELIMITER)
	if len(data) != 2:
		return () 
	return (data[0], float(data[1]))

def emit(key, value):
	print key + DELIMITER + str(value)

lastKey = None
largestSale = -1

for line in sys.stdin:
	data = parseLine(line)
	if len(data) == 0:
		continue

	newKey = data[0]
	newValue = data[1]
		
	if (lastKey and lastKey != newKey):
		# emit and update newKey if we are done reducing values for the previous key
		emit(lastKey, largestSale)
		largestSale =-1
		lastKey = newKey
	# necessary to initialize lastKey without using a flag/conditionals
	lastKey = newKey
	if newValue > largestSale:
		largestSale = newValue

# emit result for last key if it exists
if lastKey:
	emit(lastKey, largestSale)
