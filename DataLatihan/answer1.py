data1 = "Data1.txt"

def readData(data1):
	x = []
	with open(data1) as data :
	    for line in data :
	    	x = line.split()
	return x


teks1 = readData(data1)

isi = []
for i in teks1 :
	if i == 'I' :
		isi.append('*')
	elif i == 'and' or i == 'The' or i=='you':
		isi.append('*'*3)
	else :
		isi.append(i)

asd = ' '.join(isi)
print (asd)
