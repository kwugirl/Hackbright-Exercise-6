from sys import argv

script, filename = argv

# opens the file and makes it one string that keeps the new lines
text = open(filename).read()

# splits the text string by the lines into a list of lines
lineList = text.splitlines()

wordList = []

for i in lineList:
	words = i.split(' ')
	for j in range(len(words)):
		words[j] = (words[j].strip('?.*[]()1234567890,')).lower()
	wordList += words
# now we have a list, wordList of all the words in the file, converted to lowercase

wordDict = {}

"""
# this is the same for loop to add keys and counts to the dictionary, just using the get method
for word in wordList:
	if wordDict.get(word, 0) == 0:
		wordDict[word] = 1
	else:
		wordDict[word] += 1
"""

for word in wordList:
	if word not in wordDict:
		wordDict[word] = 1
	else:
		wordDict[word] += 1

for key, value in sorted(wordDict.iteritems(), key=lambda (k,v): (v,k)):
    print "%s: %s" % (key, value)

