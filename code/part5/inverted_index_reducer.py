#!/usr/bin/python

import sys

DELIMITER = '\t'

def parseLine(line):
    return line.strip("\n").split(DELIMITER)

def emit(kvp):
    print kvp[0] + DELIMITER + kvp[1]

# Reduce("word", [nodes]) -> [unique_nodes])
def reducer():
    currWord = None
    nodes = set()

    for line in sys.stdin:
        data = parseLine(line)
        if currWord is None:
            currWord = data[0]

        if currWord == data[0]:
            if data[1] not in nodes:
                nodes.add(data[1])
        else:
            res = ""
            for node in nodes:
                res += node + " "
            emit(currWord, res)
            nodes.clear()

    if currWord:
        # at least one word in stream
        # since last word is not emitted
        res = ""
        for node in nodes:
            res += node + " "
        emit(currWord, res)

def main():
    reducer()

if __name__ == "__main__":
    main()