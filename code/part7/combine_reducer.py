#!/usr/bin/python

import sys
import csv

DELIMITER = '\t'

# determine data source
def whichDataSource(lenData):
    if lenData == 19:
        # B represents the post data source
        return "B"
    elif lenData == 5:
        # A represents the user data source
        return "A"

# Reduce("10000B....", "postData") -> (postData combined with user data, postData combined with user data, ...)
def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    currUser = None
    userInfo = None
    for line in reader:
        if currUser == line[0][:-1]:
            # same user
            output = line[1:] + userInfo
            writer.writerow(output)
        else:
            currUser = line[0][:-1]
            userInfo = line[1:]

        
def main():
    reducer()

if __name__ == "__main__":
    main()
    