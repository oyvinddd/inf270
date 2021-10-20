###############################
##   NAME: ØYVIND HAUGE      ##
##   PYTHON VERSION: 3.8.5   ##
###############################

# 1. Dualization

def dualize(A, b, c):
    m, n = len(A), len(A[0])
    new_A = [[0 for _ in range(m)] for _ in range(n)]
    # create negative transposed matrix
    for i in range(m):
        for j in range(n):
            new_A[j][i] = A[i][j] * -1
    # c in (P) is equal to b in (D)
    # multiply by -1 to put in standard form
    b_new = [x * -1 for x in c]
    # b in (P) is equal to c in (D)
    # multiply by -1 to put in standard form
    c_new = [x * -1 for x in b]
    return new_A, b_new, c_new


# 2. LU-decomposition

def LU_decompose(A):
    m = len(A)
    # initialize empty lower/upper matrices
    L = [[0 for _ in range(m)] for _ in range(m)]
    U = [[0 for _ in range(m)] for _ in range(m)]
    for row_idx in range(m):
        eliminate(A, row_idx, row_idx)
    return L, U


# Utility functions

def print_matrix(A):
    m = len(A)
    for row_idx in range(m):
        row_str = ''
        for col_idx in range(m):
            row_str += '{:8.1f}'.format(A[row_idx][col_idx])
        print(row_str)

A = [
    [2, 0, 4, 0, -2],
    [3, 1, 0, 1, 0],
    [-1, 0, -1, 0, -2],
    [0, -1, 0, 0, -6],
    [0, 0, 1, 0, 4]
]


def eliminate(A, pivot_row, pivot_col):
    m, c = len(A), 0
    for row_idx in range(pivot_row + 1, m):
        c = A[row_idx][pivot_col] / A[pivot_row][pivot_col]
        if c != 0:
            for col_idx in range(m):
                A[row_idx][col_idx] = A[row_idx][col_idx] - c * A[pivot_row][col_idx]


#c = b[0] / a[0]
#for i in range(len(a)):
#    b[i] = b[i] - c * a[i]
print_matrix(A)

print("      ##################################")

LU_decompose(A)

print_matrix(A)

#L, U = LU_decompose(A)
#print_matrix(L)
