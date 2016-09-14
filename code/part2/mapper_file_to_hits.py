#!/usr/bin/python

# Maps page to number of hits.

# Map("log_chunk_2", "10.22.33...") -> [("1.1.1.1", 1),...,("1.1.1.1",2)]


import sys
import re


REGEX_COMMON_LOG_FORMAT = '(^[(\d{1,3}\.)]+\d{1,3}) (.+) (.+) \[(\d{2}/\w{3}/\d{4}):(\d{2}:\d{2}:\d{2}) -(\d{4})] "(\w+) (.+) ([\w\\/\.]+)[ ]*" (\d{3}) (-|\d+)$'

REGEX_URL = '^(https?:\/\/[\)\(\;\,\+\*\'\&\$\!\@\]\[\~\#\?:\=\_\w\d\-\.]*)?(\/.*)?$'

def parseLine(line):
	line = line.strip('\n')
	return re.match(REGEX_COMMON_LOG_FORMAT, line).groups()

def stripURL(url):
	parts = re.match(REGEX_URL, url).groups()
	if parts[1]  == None:
		parts = (parts[0], '\\')
	return parts
for line in sys.stdin:
	data = parseLine(line)
	file = stripURL(data[7])[1]
	print file + '\t' + "1"	
