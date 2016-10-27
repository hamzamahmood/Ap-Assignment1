import csv		# imports the csv module

dict = {"":[]}
f = open('Frequency_NoChains.csv','wb')
writer = csv.writer(f)
writer.writerow(["Word Length","Frequency of Words With No Chain"])
writer.writerow(["1","0"])
for WordSize in range(2,36):
	count = 0
	f = open('No_Chains/No_Chains'+str(WordSize)+'.csv','rb')
	csv_f = csv.reader(f)
	c = 0
	for row in csv_f:
		if c == 0:
			c += 1
			continue
		count += 1
	writer.writerow([WordSize,count])