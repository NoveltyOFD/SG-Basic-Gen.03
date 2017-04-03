import numpy as novel

M = novel.mat("0,0,-2;1,2,1;1,0,3")
eigenvalue,eigenvector = novel.linalg.eig(M)
print(eigenvalue)
print(eigenvector)