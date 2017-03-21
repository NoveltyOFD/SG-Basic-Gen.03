<<<<<<< HEAD
data1 = "Data1.txt"
=======
data1 = "Data_1.txt"
data2 = "Data_2.txt"
>>>>>>> 3a5b3855996f95c32312d96cf20520b45a49027c

def readData(data1):
	x = []
	with open(data1) as data :
	    for line in data :
<<<<<<< HEAD
	    	x = line.split()
	return x


x = readData(data1)

b = []
for i in x :
	if i == 'I' :
		b.append('*')
	elif i == 'and' or i == 'The' or i=='you':
		b.append('*'*3)
	else :
		b.append(i)

asd = ' '.join(b)
print (asd)
=======
		    x = line.split()
	return x
>>>>>>> 3a5b3855996f95c32312d96cf20520b45a49027c
