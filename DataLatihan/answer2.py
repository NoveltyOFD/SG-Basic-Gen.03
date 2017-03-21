data1 = "Data1.txt"
data2 = "Data2.txt"

def readData(data1):
	x = []
	with open(data1) as data :
	    for line in data :
		    x = line.split()
	return x

teks1 = readData(data1)
teks2 = readData(data2)

same = []

for x in teks1 :
	for y in teks2:
		if x==y :
			counter = 0
			for z in same :
				if z == y :
					counter += 1
			if counter == 0 :
				same.append(y)

print (same)