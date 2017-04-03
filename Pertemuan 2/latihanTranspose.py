import numpy as novel
matriks = [[12,7],[4,5],[3,8]]
#transpose = [list(x) for x in zip(*matriks)]

#for x in transpose:
#	print(x)

# print(novel.transpose(matriks))


M = novel.mat("1 -2;1 4")
M = novel.mat("1 -2;1  4")

eigenvalue,eigenvector = novel.linalg.eig(M)
print(eigenvalue)