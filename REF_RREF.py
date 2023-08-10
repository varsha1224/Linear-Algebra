# REF AND RREF

def is_ref(matrix):
    row = len(matrix)
    col = len(matrix[0])

    # Check for leading zeros
    leading_zeros = []
    first_non_zero = []
    for i in range(row):
        leading_zero_count = 0
        for j in range(col):
            if matrix[i][j] != 0:
                first_non_zero.append(matrix[i][j])
                break
            leading_zero_count += 1
        leading_zeros.append(leading_zero_count)

    # Check for row echelon form
    for i in range(row - 1):
        if leading_zeros[i] > leading_zeros[i + 1]:
            return False
        
    for item in first_non_zero:
        if item != 1:
            return False

    return True


def is_rref(matrix):
    row = len(matrix)
    col = len(matrix[0])

    if is_ref == False:
        return False
    
    # Check for leading zeros
    first_non_zero_index = []
    for i in range(row):
        for j in range(col):
            if matrix[i][j] != 0:
                first_non_zero_index.append(j)
                break

    # Check for exactly one leading one in each column
    for j in first_non_zero_index:
        leading_one_count = 0
        for i in range(row):
            if matrix[i][j] == 1:
                leading_one_count += 1
            elif matrix[i][j] != 0:
                return False  # Non-zero element not in leading one column
        if leading_one_count != 1:
            return False  # Leading one count not equal to 1

    return True


def print_matrix(matrix):
    for row in matrix:
        print(row)

matrix1 = [[1, 2, 5, 3, 0],
           [0, 0, 1, 1, 0],
           [0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]]
print("Matrix (a):")
print_matrix(matrix1)
print("REF:", is_ref(matrix1))
print("RREF:", is_rref(matrix1))


