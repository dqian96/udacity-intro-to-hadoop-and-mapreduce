#!/usr/bin/python

import re
import sys
import csv

# parse a forum post body for words (i.e. alphanumeric chars)
def parseBody(body):
    words = re.findall(r"([a-zA-Z]+)", body)
    return words

def emit(key, value):
    print key + '\t' + value

# mapper 
#(forumFileChunk, "<p>asdasdd....") -> [("dog", 1), ("rock", 2),...]
def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    for post in reader:
    postBody = post[4]
        nodeId = post[0]
        words = parseBody(postBody)
    for word in words:
            emit(word.lower(), nodeId)

def main():
    mapper()

if __name__ == "__main__":
    main()