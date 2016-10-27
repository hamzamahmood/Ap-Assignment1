import json		# imprts the json module to read the dictionary
import csv		# imports the csv module
import sys		# imports the sys module


myList = []
with open('dictionary.json') as data_file:    
	data = json.load(data_file)
	myList = data.keys()
#print json.dumps(myList, indent=4, sort_keys=True)
#print len(myList)

word_length = []
for word in myList:
	#print json.dumps(word, indent=4, sort_keys=True),len(word)
	length = len(word)
	if not length in word_length:
		word_length.append(length)
word_length.sort()
print word_length


for WordSize in range(1,36):
	myList2 = []
	for word in myList:
		if len(word) == WordSize:
			myList2.append(word)
	print "No of ",WordSize," words: ",len(myList2)