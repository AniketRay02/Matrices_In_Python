def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    transposed = [[0 for j in range(rows)] for i in range(columns)]

    for i in range(rows):
        for j in range(columns):
            transposed[j][i] = matrix[i][j]

    return transposed


def powers(lst, start, end):
    # lst - list of numbers
    # start - integer that
    matrix = []
    for num in lst:
        row = [num ** p for p in range(start, end + 1)]
        matrix.append(row)
    return matrix


def matmul(A, B):  # Defining function matmul that takes two matrices 'A' and 'B'
    rows_A = len(A)
    columns_A = len(A[0])
    rows_B = len(B)
    columns_B = len(B[0])
    # These lines store the number of rows and columns respectively
    if columns_A != rows_B:
        raise ValueError
    # This checks if the numbers of columns in A is equal to rows in B. If not equal then it raises ValueError which
    # says that the two matrices can't be multiplied

    C = [[0 for j in range(columns_B)] for i in range(rows_A)]
    # Creates a new matrix C with rows_A and columns_B, and initializes all elements of the matrix to 0
    for i in range(rows_A):
        for j in range(columns_B):
            for k in range(columns_A):
                C[i][j] += A[i][k] * B[k][j]
    # Performs the matrix multiplication
    return C

def invert(A):
    a, b, c, d, = A[0][0], A[0][1], A[1][0], A[1][1]
    determinant = a * d - b * c
    if determinant == 0:
        raise ValueError
    return [[d / determinant, -b / determinant], [-c / determinant, a / determinant]]


def loadtxt(filename):
    data = []
    with open(filename) as i:
        for line in i:
            line_data = [float(x) for x in line.split()]
            data.append(line_data)
    return data

