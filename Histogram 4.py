from collections import Counter
import re

def openfile(Filename):
    fh = open("TEXT.txt", "r+")
    str = fh.read()
    fh.close()
    return str

def removegarbage(str):
    str = re.sub(r'\W+', ' ', str)
    str = str.lower()
    return str

def getwordbins(words):
    cnt = Counter()
    for word in words:
        cnt[word] += 1
    return cnt

def main(Filename, topwords):
    txt = openfile("TEXT.txt")
    txt = removegarbage(txt)
    words = txt.split(' ')
    bins = getwordbins(words)
    for key, value in bins.most_common(topwords):
        print (key,value)

main('speech.txt', 500)