# Matrix Algebra

import numpy as np

A = np.matrix([[1,2,3],[2,7,4]])
B = np.matrix([[1,-1],[0,1]])
C = np.matrix([[5,-1],[9,1],[6,0]])
D = np.matrix([[3,-2,-1],[1,2,3]])
u = np.matrix([6,2,-3,5])
v = np.matrix([3,5,-1,4])
w = np.matrix([[1],[8],[0],[5]])

print(A.shape)
#1.1) (2,3)

print(B.shape)
#1.2) (2,2)

print(C.shape)
#1.3) (3,2)

print(D.shape)
#1.4) (2,3)

print(u.shape)
#1.5) (1,4)

print(w.shape)
#1.6) (4,1)

print(u+v)
#2.1) [9,7,-4,9]

print(u-v)
#2.2) [3,-3,-2,1]

print(6*u)
#2.3) [36 12 -18 30]

print(np.vdot(u,v))
#2.4) 18

print(np.linalg.norm(u))
#2.5) 8.6

#print(A+C)
#3.1)not defined

print(A-np.transpose(C))
#3.2) [[-4,-7,-3],[3,6,4]]

print(np.transpose(C) + 3*D)
#3.3) [[14,3,3],[2,7,9]]

print(B*A)
#3.4) [[-1,-5,-1],[2,7,4]]

#print(B*np.transpose(A))
#3.5)not defined

#print(B*C)
#3.6)not defined

print(C*B)
#3.7) [[5,-6],[9,-8],[6,-6]]

print(np.linalg.matrix_power(B,4))
#3.8) [[1,-4],[0,1]]

print(A*np.transpose(A))
#3.9) [[14,28],[28,69]]

print(np.transpose(D)*D)
#3.10) [[10,-4,0],[-4,8,8],[0,8,10]]

