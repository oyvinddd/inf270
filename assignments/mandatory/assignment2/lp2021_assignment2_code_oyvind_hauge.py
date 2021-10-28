###############################
##   NAME: ØYVIND HAUGE      ##
##   PYTHON VERSION: 3.8.5   ##
###############################

# 1.1 Dualization

def dualize(A, b, c):
    m, n = len(A), len(A[0])
    new_A = [[0 for _ in range(m)] for _ in range(n)]
    # create negative transposed coefficient matrix
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


# 1.2 LU-decomposition

def LU_decompose(A):
    # exit early if input matrix is not a square matrix
    if not is_square_matrix(A):
        return [], []
    n = len(A)
    # initialize empty lower triangular matrix
    L = [[0 for _ in range(n)] for _ in range(n)]
    for pivot in range(n):
        # add the diagonal (pivot) values to L (multiply by the inverse to get only 1's)
        L[pivot][pivot] = A[pivot][pivot] * 1 / A[pivot][pivot]
        # do row reduction
        for row in range(pivot + 1, n):
            c = A[row][pivot] / A[pivot][pivot]
            if c != 0:
                for col in range(pivot, n):
                    # if coefficient is non-zero it should be added to L
                    L[row][pivot] = c
                    # subtract value in each column with a given
                    # multiplier of the column in the pivot row
                    A[row][col] = A[row][col] - c * A[pivot][col]
    # in the end, the altered values in A make up the matrix U.
    # that is why we just return A instead of creating a new matrix U.
    return L, A


# Utility functions

# Checks if a given input matrix is a square matrix
def is_square_matrix(A):
    n = len(A)
    for row in A:
        if len(row) != n:
            return False
    return n > 0


# Prints a given input matrix to the console
def print_matrix(A):
    m = len(A)
    for row_idx in range(m):
        row_str = ''
        for col_idx in range(m):
            row_str += '{:12.2f}'.format(A[row_idx][col_idx])
        print(row_str)


# Execute program

# example from the book
A = [[2, 0, 4, 0, -2], [3, 1, 0, 1, 0], [-1, 0, -1, 0, -2], [0, -1, 0, 0, -6], [0, 0, 1, 0, 4]]

print("#################################################")

L, U = LU_decompose(A)

print_matrix(L)

print("#################################################")

print_matrix(U)

print("#################################################")
