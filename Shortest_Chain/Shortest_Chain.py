import json		# imprts the json module to read the dictionary
import csv		# imports the csv module
import sys		# imports the sys module


myList = []
with open('dictionary.json') as data_file:    
	data = json.load(data_file)
	myList = data.keys()
#print json.dumps(myList, indent=4, sort_keys=True)
print len(myList)

for WordSize in range(1,36):
	explored = []
	print "Loading myList2 of ",WordSize
	myList2 = []
	for word in myList:
		if len(word) == WordSize:
			myList2.append(word)
	print "Loading Done!"
	fname = "Shortes_Chain_temp"+str(WordSize)+".csv"
	f = open(fname, 'wb') # opens the csv file

	writer = csv.writer(f)  # creates the reader object
	writer.writerow(["word","conversion","chain length"])
	for word in myList2:
		explored.append(word)
		for loc in range(WordSize):
			for letter in range(65,90):
				wd = list(word)
				wd[loc] = chr(letter)
				wd = "".join(wd)
				if((wd not in explored) and (wd in myList2)):
					writer.writerow([word,wd,'1'])
	print "Done ",WordSize
	f.close()