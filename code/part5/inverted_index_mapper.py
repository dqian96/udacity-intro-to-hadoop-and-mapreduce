#!/usr/bin/python

# parse a forum post body for words (i.e. alphanumeric chars)
def parseBody(body):
    words = re.findall(r"[\w']+", body)
    return words

def emit(key, value):
    print key + '\t' + value

# mapper 
#(forumFileChunk, "<p>asdasdd....") -> [("dog", 1), ("rock", 2),...]
def mapper(forumDataFilePath):
    forumDataFile = open(forumDataFilePath, 'r')
    for post in forumDataFile:
        postBody = post[4]
        nodeId = post[0]
        words = parseBody(postBody)
        for word in words:
            print emit(word, nodeId)

def main():
    mapper(\
        "~/coding/udacity-intro-to-hadoop-and-mapreduce/"+\
        "data/formula_node.tsv", "r"\
        )

if __name__ == "__main__":
    main()