#!/usr/bin/python

# Find the highest sale per store
# i.e. ("BB", 120000)

# Map("blk_i", "2012-05-03	17:59...") -> [("Walmart", 2300),..., ("Starbucks",320)]

import sys

DELIMITER = '\t'

def parseLine(line):
	data = line.strip("\n").split(DELIMITER)
	# Parsing error
	if len(data) != 6:
		return []
	return data

def emit(key, value):
	print key + DELIMITER + value

for line in sys.stdin:
	data = parseLine(line)
	if len(data) == 0:
		continue
	else:
		emit(data[2], data[4])		
