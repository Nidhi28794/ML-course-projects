# this module will be imported in the into your flowgraph
import numpy as np
from scipy.linalg import svd
h = np.zeros((16,16))
for i in range (0,16):
	for j in range(0,16):
		if((i+j)%8 == 2):
			h[i,j] = 1
for i in range (0,16):
	for j in range(0,16):
		if((i+j)%8 == 1):
			h[i,j] = 1

for i in range (8,16):
	for j in range(8,16):
		if((i+j)%8 == 1):
			h[i,j] = -1
U,s,V = svd(h) 
UT = np.transpose(U);
a=UT.tolist();
b=V.tolist();
