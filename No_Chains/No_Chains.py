import json		# imprts the json module to read the dictionary
import csv		# imports the csv module
import sys		# imports the sys module


myList = []
with open('dictionary.json') as data_file:    
	data = json.load(data_file)
	myList = data.keys()
#print json.dumps(myList, indent=4, sort_keys=True)
#print len(myList)

# word_length = []
# for word in myList:
# 	#print json.dumps(word, indent=4, sort_keys=True),len(word)
# 	length = len(word)
# 	if not length in word_length:
# 		word_length.append(length)
# word_length.sort()
# print word_length

for WordSize in range(5,36):
	explored = []
	print "Loading myList2 of ",WordSize
	myList2 = []
	for word in myList:
		if len(word) == WordSize:
			myList2.append(word)
	print "Loading Done!"
	count = 0
	fname = "No_Chains"+str(WordSize)+".csv"
	f = open(fname, 'wb') # opens the csv file

	writer = csv.writer(f)  # creates the reader object
	writer.writerow(["Word"])
	for word in myList2:
		count = 0
		explored.append(word)
		for loc in range(WordSize):
			for letter in range(65,90):
				wd = list(word)
				wd[loc] = chr(letter)
				wd = "".join(wd)
				if((wd not in explored) and (wd in myList2)):
					count += 1
					break
			if(count == 1):
				break
		if(count == 0):
			#print word
			writer.writerow([word])
print "Done ",WordSize
f.close()