from sys import argv

script, filename = argv

# opens the file and makes it one string that keeps the new lines
text = open(filename).read()

# splits the text string by the lines into a list of lines without the newlines
lineList = text.splitlines()

# create wordList as a list
wordList = []

# punctuation that should get stripped out
punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

# function to remove all punctuation from words, not just from the ends
def remove_punctuation(s):
    s_sans_punct = ""
    for letter in s:
        if letter not in punctuation:
            s_sans_punct += letter
    return s_sans_punct


# go through each line in the list of lines
for i in lineList:
	# split it out into words based on the space
	words = i.split(' ')
	
	# strip out characters/numbers from the words and convert it to lowercase
	for j in range(len(words)):
		words[j] = remove_punctuation(words[j]).lower()
		
		# previously used "(words[j].strip('?.*[]()1234567890,-_!;')).lower()" but string.strip method only strips out characters at the beginning or end of the string, not in the middle
		
	# add the word to the wordList list
	wordList += words
# now we have a list, wordList of all the words in the file, converted to lowercase

# create wordDict as a dictionary
wordDict = {}

"""
# this is the same for loop to add keys and counts to the dictionary, just using the get method
for word in wordList:
	if wordDict.get(word, 0) == 0:
		wordDict[word] = 1
	else:
		wordDict[word] += 1
"""

# go through each word in the wordList list
for word in wordList:
	# if the word isn't already in the dictionary, add it as a key and set the value to 1
	if word not in wordDict:
		wordDict[word] = 1
	# if the word is already in the dictionary, just increment the value by 1
	else:
		wordDict[word] += 1

# print out contents of dictionary from highest value to lowest value and for lines with the same value, sort by key alphabetically
# sorted is a Python function that can be used on various objects like lists
# "key=lambda (k, v): (v, k)" sorts by the values rather than just by the keys. Lambda is an anonymous function created on the fly at runtime, here it's a function that takes in (k, v) as arguments and then returns them as v, k.
# used "key=lambda (k, v): (v, k), reverse=True" to sort by descending rather than ascending value, but then this also sorted the keys reverse alphabetically too, so use -v to sort by negative of value to be able to still sort keys alphabetically ascending
for key, value in sorted(wordDict.iteritems(), key=lambda (k, v): (-v, k)):
    print "%s: %s" % (key, value)

""" the equivalent of the lambda function used in the dictionary print loop "lambda (k, v): (v, k)"
def lambda_real (key, value):
	# print "first line of function", key, value
	return value, key
	
print lambda_real("f-key", "f-value")
"""