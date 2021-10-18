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


def print_matrix(M):
    for index, row in enumerate(M):
        print(row)


A = [
    [-1, -1],
    [-1,  1],
    [ 1,  2]
]
b = [-3, -1, 2]
c = [1, 3]

A_new, b_new, c_new = dualize(A, b, c)
print_matrix(A_new)
print("#######")
print_matrix(b_new)
print("#######")
print_matrix(c_new)
