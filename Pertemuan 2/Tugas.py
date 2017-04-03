matriks1 = [[1,2,3],[4,5,6],[7,8,9]]
matriks2 = [[1],[2],[3]]

test = []
test1 = []
test2 = []
test3 = []
temp = 0
 
y=0
for a in matriks1:
	counter1 =0
	y += 1
	x =0
	for b in a:
		counter1+=1
		counter2 = 0
		for c in matriks2 :
			for d in c:	
				counter2 += 1
				if counter1==counter2 :
					x += (b*d)
	if (y==1):
		test1.append(x)
	elif (y==2):
		test2.append(x)
	elif (y==3):
		test3.append(x)

test.append(test1)
test.append(test2)
test.append(test3)

print (test)
