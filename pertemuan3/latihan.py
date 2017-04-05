test = ['(','(',')']

simpan = []

cek = "tidak valid"

for i in test:
	if (i == '(' ):
		simpan.append(i)
	elif (i == ')'):
		if (len(simpan) != 0 ):
			for n in simpan:
				if (n == '('):
					cek ="valid"
					simpan.remove(n)
					break
				elif (n != ')'):
					cek = "tidak valid"
					break
		elif (len(simpan) == 0):
			cek = "tidak valid"

if (len(simpan)!= 0):
	cek = "tidak valid"
	
print(cek)