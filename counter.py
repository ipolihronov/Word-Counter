#!/usr/bin/python3

import sys
import urllib.request
import os.path
import hashlib
from myLib import downloadBook

uniqueWords = {}
topWords = {}
allWords = []
excludedWords = []

defaultTopPrint = 50
bookCheckSum = "2c89aeaa17956a955d789fb393934b9a"
bookUrl = "http://www.gutenberg.org/files/2600/2600-0.txt"
wordCount = 0

def removePunctuation():
    global wordCount
    for line in text:
        for word in line.split():
            wordCount = wordCount + 1
            if word not in excludedWords:
                word = word.lower()
                word = word.replace(".","")
                word = word.replace(",","")
                word = word.replace("!","")
                word = word.replace(":","")
                word = word.replace("?","")
                word = word.replace("*","")
                allWords.append(word)

def isBookHere():
    bookHere = False
    for file in os.listdir("."):
        if file.endswith(".txt"):
            if bookCheckSum == hashlib.md5(open(file, 'rb').read()).hexdigest():
                bookHere = True
                print ("the book is here!")
                break
    return bookHere

def printResults():
    print ("word --> occurances")
    print ("*******************************")
    numberOfWords = int(sys.argv[1] if len(sys.argv) >= 2 else defaultTopPrint)
    topWords = sorted(uniqueWords.items(), key=lambda x:-x[1])[:numberOfWords]
    for word, count in topWords:
        print ("%s --> %s" %(word, count))
    print ("*******************************")
    print ("*******************************")
    print ("total words : %d" %wordCount)

if not isBookHere():
    downloadBook()

text = open("book.txt", "r")
badWords = open("badWords.txt", "r")

removePunctuation()

for word in allWords:
    if word not in uniqueWords:
        uniqueWords[word] = 1
    else:
        uniqueWords[word] = uniqueWords[word] + 1

printResults()
