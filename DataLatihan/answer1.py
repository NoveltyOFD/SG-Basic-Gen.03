data1 = "Data1.txt"

def readData(data1):
	x = []
	with open(data1) as data :
	    for line in data :
	    	x = line.split()
	return x


teks1 = readData(data1)

b = []
for i in teks1 :
	if i == 'I' :
		b.append('*')
	elif i == 'and' or i == 'The' or i=='you':
		b.append('*'*3)
	else :
		b.append(i)

asd = ' '.join(b)
print (asd)
