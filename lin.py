import numpy as np
M=np.array([[1,2,3],[-4,5,6],[7,-8,9]])
V=np.array([[1,2,3],[9,6,7],[1,1,1]])
print"Type of M:\n",M.shape
#Transpose of M
print"Transpose of M:\n",M.T
#Inverse of M
print"Inverse of M:\n",np.linalg.det(M)
#Determinent of M
print"Det of M:\n",np.linalg.det(M)
#Eigenvalues and Eigenvectors
eigvals,eigvecs=np.linalg.eig(M)
print"Eigvals:\n",eigvals
print"Eigvecs:\n",eigvecs
#Matrix dot product
print"Matrix dot product:\n",M.dot(V)
#Matrix cross product
print"Matrix cross product:\n",np.cross(M,V)
#Rank of matrix M
print"Rank of M:\n",np.linalg.matrix_rank(M)
#Trace of matrix M
print"Trace of M:\n",np.trace(M)
#Raise matrix to power 3
print"Matrix M raised to power 3:\n",np.power(M,3)
#Solve equations
print"Linear equations solutions:\n",np.linalg.solve(M,V)
#Norm of M
print"Norm of M:\n",np.linalg.norm(M)
#Absolute of M
print"Absolute of M:\n",np.abs(M)
#Maximum and minimum of M
print"Maximun of M:\n",np.max(M)
print"Minimum of M:\n",np.min(M)
#Array math
print"Addition of M and V:\n",np.add(M,V)
print"Subtraction of M and V:\n",np.subtract(M,V)
print"Multiplication of M and V:\n",np.multiply(M,V)
print"Division of M and V:\n",np.divide(M,V)

