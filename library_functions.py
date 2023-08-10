# SOLUTION USING LIBRARY FUNCTIONS

import numpy as np
import sympy as sp

n = int(input("Enter the number of rows : "))
print("Enter A")
A = [[int(input()) for j in range (n)] for i in range (n)]
print("Enter B")
B = [int(input()) for i in range (n)]

matrix = sp.Matrix(A)

print("RREF:", matrix.rref()[0])

print("RANK:", np.linalg.matrix_rank(A))

matrix = np.array(A)
eigVal, eigVec = np.linalg.eig(matrix)
print("Eigen Vectors :", eigVec)
print("Eigen Values :", eigVal)

print("Inverse:\n", np.linalg.inv(A))

print("Dot:\n", np.dot(A, B))

print("Solve:\n", np.linalg.solve(A, B))
