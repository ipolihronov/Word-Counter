#text = open("text.txt", "r")
text = open("2600-0.txt", "r")
badWords = open("badWords.txt", "r")
wordCount = 0

uniqueWords = {}
topWords = {}

allWords = []
excludedWords = []

for line in badWords:
    for word in line.split(','):
        word = word.replace(" ","")
        excludedWords.append(word)

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

for word in allWords:
    if word not in uniqueWords:
        uniqueWords[word] = 1
    else:
        uniqueWords[word] = uniqueWords[word] + 1

print "word --> occurances"
print "*******************************"
topWords = sorted(uniqueWords.iteritems(), key=lambda x:-x[1])[:50]
for word, count in topWords:
    print "%s --> %s" %(word, count)
print "*******************************"
print "*******************************"
print "total words : %d" %(wordCount)
