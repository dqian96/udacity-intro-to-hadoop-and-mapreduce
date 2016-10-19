#!/usr/bin/python

import sys

DELIMITER = '\t'

def parseLine(line):
    return line.strip("\n").split(DELIMITER)

def emit(key, value):
    print key + DELIMITER + value

# Reduce("word", [nodes]) -> [unique_nodes])
def reducer():
    currWord = None
    nodes = set()
    count = 0
    for line in sys.stdin:
        data = parseLine(line)
        # change words
        if currWord and currWord != data[0]:
            res = "Nodes: "
            for node in nodes:
                res += node + " "
            res += "Count: " + str(count)
            emit(currWord, res)
            nodes.clear()
            currWord = data[0]
            count = 0
        # same word
        if currWord is None or currWord == data[0]:
            currWord = data[0]
            count += 1
        if data[1] not in nodes:
            nodes.add(data[1])
    
    if currWord:
        # at least one word in stream
        # since last word is not emitted
        res = "Nodes: "
        for node in nodes:
            res += node + " "
        res += "Count: " + str(count)
        emit(currWord, res)

def main():
    reducer()

if __name__ == "__main__":
    main()