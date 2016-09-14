#!/usr/bin/python

# From a list of ("file", hits) pairs, we reduce them such that if the
# hits for a particular file is not the largest, it will be an empty
# mapping.
# For the file with the max hits, the number of hits will be
# returned/mapped.
# This is a reducer that only returns for the max key, and reduces with
# empty for non-max keys.

# Reduce("fb.com", [1,1,1]) -> None (empty mapping/return as it's not max)
# Reduce("yahoo.com", [1,1]) -> None (empty mapping/return as it's not max)
# Reduce("google.com", [1,1,1,1]) -> 4 (returns number of total hits as it is the max)


import sys

lastKVP = None
# dummy values
maxKVP = ('', -1)

DELIMITER = '\t'

def parseLine(line):
	return line.strip("\n").split(DELIMITER)

def emit(kvp):
	print kvp[0] + DELIMITER + str(kvp[1])

for line in sys.stdin:
	data = parseLine(line)
	if lastKVP:
		if data[0] == lastKVP[0]:
			lastKVP = (lastKVP[0], lastKVP[1] + int(data[1]))
			continue
		else:
			if lastKVP[1] > maxKVP[1]:
				maxKVP = lastKVP
	lastKVP = (data[0], int(data[1]))

if lastKVP:
	if lastKVP[1] > maxKVP[1]:
		maxKVP = lastKVP
	emit(maxKVP)	
