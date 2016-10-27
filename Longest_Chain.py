import csv		# imports the csv module

f = open('Longest_Chains.csv','wb')
writer = csv.writer(f)
writer.writerow(["Word Length","Size of Chain"])
for WordSize in range(2,36):
	f = open('Chains/Chains'+str(WordSize)+'.csv', 'rb')
	csv_f = csv.reader(f)
	c = 0
	max = 0
	for row in csv_f:
		if c == 0:
			c += 1
			continue
		word,conversion,hops = row
		h = int(hops)
		h -= 1
		if(h>max):
			max = h
	#print WordSize,max
	writer.writerow([WordSize,max])
f.close()
