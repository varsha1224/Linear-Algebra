# INVERSE POWER METHOD

def powerMethod(matrix, it):
    n = len(matrix)
    x = [1.0] * n
    for _ in range (it):
        Ax = [sum(matrix[i][j] * x[j] for j in range (n)) for i in range(n)]
        minElement = min(Ax)
        x = [element / minElement for element in Ax]
    return x

def rayleigh(matrix, vec):
    n = len(matrix)
    nr = sum(matrix[i][j] * vec[i] * vec[j] for j in range (n) for i in range (n))
    dr = sum(vec[i]**2 for i in range(len(vec)))
    return nr/dr

matrix = [[1, 2, 0],
          [-2, 1, 2],
          [1, 3, 1]]
it = 100

eigVec = powerMethod(matrix, it)
print("Eigen vector = ", eigVec)
print("Eigen value = ", rayleigh(matrix, eigVec))