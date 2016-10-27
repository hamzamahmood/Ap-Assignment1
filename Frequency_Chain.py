import csv		# imports the csv module

dict = {"":[]}
for WordSize in range(2,36):
    f = open('Chains/Chains'+str(WordSize)+'.csv', 'rb')
    csv_f = csv.reader(f)
    c = 0
    for row in csv_f:
        if c == 0:
            c += 1
            continue
        word,conversion,hops = row
        temp = int(hops)
        temp -= 1
        h = str(temp)
        if not h in dict:
        	dict[h] = [h]
        else:
        	dict[h].append(h)

f = open('Frequency.csv','wb')
writer = csv.writer(f)
writer.writerow(["No of Hops Taken","Frequency of Words"])
for a in dict:
    if not(len(dict[a]) == 0):
	   #print a,len(dict[a])
       writer.writerow([a,len(dict[a])])