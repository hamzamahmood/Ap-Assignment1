import json		# imprts the json module to read the dictionary
import csv		# imports the csv module
import sys		# imports the sys module


myList = []
with open('dictionary.json') as data_file:    
	data = json.load(data_file)
	myList = data.keys()
#print json.dumps(myList, indent=4, sort_keys=True)
#print len(myList)

for WordSize in range(2,36):
	explored = []
	dict = {"":[]}
	fname = 'Shortest_Chain/Shortes_Chain'+str(WordSize)+'.csv'
	fe = open (fname,'rb')
	reader = csv.reader(fe)
	c = 0
	print "Loading LegalConversions dictionary for word length: ",WordSize
	for row in reader:
		if c == 0:
			c += 1
			continue
		a,b,c = row
		a = "".join(a)
		b = "".join(b)
		if(a not in dict):
			dict[a] = [b]
		else:
			dict[a].append(b)
	print "LegalConversions dictionary loaded with length: ",len(dict)
	print "Loading myList2 of ",WordSize
	myList2 = []
	for word in myList:
		if len(word) == WordSize:
			#print word
			myList2.append(word)
	print "Loading Done!"
	fname = "Chains"+str(WordSize)+".csv"
	f = open(fname, 'wb') # opens the csv file

	writer = csv.writer(f)  # creates the reader object
	writer.writerow(["Word","Conversions","Hops"])
	for word in myList2:
		explored.append(word)
		if(word in dict):
			for word2 in myList2:
				if((word2 not in explored) and (word2 in dict)):
					Q = []
					Q.append([str(word),str(word),int(0)])
					Explored = []
					while(len(Q) != 0):
						s = Q.pop()
						if not(s[0] in Explored):
							Explored.append(s[0])
							if (s[0] == word2):
								writer.writerow([word,s[1],s[2]])
							else:
								actions = dict[word]
								for action in actions:
									if not(action in Explored):
										temp = s[1] +" "+ action
										temp2 = temp.split(" ")
										Q.append([action,temp,len(temp2)])
										lst_temp = dict[word]
	print "Done ",WordSize
	f.close()