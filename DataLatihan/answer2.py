<<<<<<< HEAD
data1 = "Data1.txt"
data2 = "Data2.txt"
=======
data1 = "Data_1.txt"
data2 = "Data_2.txt"
>>>>>>> 3a5b3855996f95c32312d96cf20520b45a49027c

def readData(data1):
	x = []
	with open(data1) as data :
	    for line in data :
		    x = line.split()
<<<<<<< HEAD
	return x

teks1 = readData(data1)
teks2 = readData(data2)

sama = []

for i in teks1 :
	for j in teks2:
		if i==j :
			counter = 0
			for x in sama :
				if x == j :
					counter += 1
			if counter == 0 :
				sama.append(j)

print (sama)
=======
return x
>>>>>>> 3a5b3855996f95c32312d96cf20520b45a49027c
