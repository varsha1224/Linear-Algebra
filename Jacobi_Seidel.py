'''def seidel(A, B, X, n):
    for i in range (n):
        temp = B[i]
        for j in range (n):
            if i != j:
                temp -= A[i][j] * X[j]
        X[i] = temp / A[i][i]
    return X

def isDiagDominant(A, n):
    for i in range (n):
        Sum = 0
        for j in range (n):
            Sum += abs(A[i][j])
        Sum -= abs(A[i][i])
        if Sum > A[i][i]:
            return False
        return True
    
n = int(input("Enter the number of rows : "))
A = [[int(input()) for j in range (n)] for i in range (n)]
B = [int(input()) for i in range (n)]


if isDiagDominant(A, n):
    if n == 3:
        X = [0, 0, 0]
        print("ITERATION\t\t\tx\ty\tz\n")
        print('%d\t\t%0.4f\t%0.4f\t%0.4f\n' %(0, X[0], X[1], X[2]))
        for i in range (25):
            X = seidel(A, B, X, n)
            print('%d\t\t\t%0.4f\t%0.4f\t%0.4f\n' %(i+1, X[0], X[1], X[2]))
        print('x=%0.4f\ty=%0.4f\tz=%0.4f\n' %(X[0], X[1], X[2]))
'''

def isDiagDominant(A, n):
    for i in range (n):
        Sum = 0
        for j in range (n):
            Sum += abs(A[i][j])
        Sum -= abs(A[i][i])
        if Sum > A[i][i]:
            return False
        return True

n = int(input("Enter the number of rows : "))
A = [[int(input()) for j in range (n)] for i in range (n)]
B = [int(input()) for i in range (n)]

print(B[0], '-', A[0][1], 'y + ', A[0][2], 'z/', A[0][0])

if isDiagDominant(A, n):
    f1 = lambda x, y, z : (B[0]-A[0][1]*y-A[0][2]*z)/A[0][0]       
    f2 = lambda x, y, z : (B[1]-A[1][0]*x-A[1][2]*z)/A[1][1]
    f3 = lambda x, y, z : (B[2]-A[2][0]*x-A[2][1]*y)/A[2][2]
    '''
    f1 = lambda x, y, z : (2-y-z)/4
    f2 = lambda x, y, z : (-6-x-2*z)/5
    f3 = lambda x, y, z : (-4-x-2*y)/3
    '''
    x0, y0, z0 = 0, 0, 0
    e = float(input("Enter error : "))
    
    c = 0
    print("ITERATION\t\t\tx\ty\tz\n")
    condition = True
    while condition:
        x1 = f1(x0, y0, z0)
        y1 = f2(x0, y0, z0)
        z1 = f3(x0, y0, z0)
        print('%d\t\t\t%0.4f\t%0.4f\t%0.4f\n' %(c, x1, y1, z1))
        
        e1 = abs(x1 - x0)
        e2 = abs(y1 - y0)
        e3 = abs(z1 - z0)
        
        c += 1
        x0 = x1
        y0 = y1
        z0 = z1
        
        condition = e1 > e and e2 > e and e3 > e
else:
    print("Not diagonally dominant")
    

