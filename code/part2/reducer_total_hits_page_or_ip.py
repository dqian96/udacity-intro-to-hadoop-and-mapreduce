#!/usr/bin/python

# Reduce("fb.com", [1,2,2]) -> 1232

import sys

oldKey = None
sum = 0

DELIMITER = '\t'

def parseLine(line):
	return line.strip("\n").split(DELIMITER)

def emit(key, value):
	print key + DELIMITER + str(value)

for line in sys.stdin:
	data = parseLine(line)
	if oldKey:
		if data[0] == oldKey:
			sum += int(data[1])
			continue
		else:
			emit(oldKey, sum)
	oldKey = data[0]
	sum = int(data[1])

if oldKey:
	emit(oldKey, sum)		
	
