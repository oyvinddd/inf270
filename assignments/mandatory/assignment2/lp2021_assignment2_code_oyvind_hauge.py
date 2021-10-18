###############################
##   NAME: ØYVIND HAUGE      ##
##   PYTHON VERSION: 3.8.5   ##
###############################

# 1. Dualization

def dualize(A, b, c):
    # create a temporary matrix containing
    # all values for A, b and c
    c.insert(0, 0)
    temp_matrix = []
    for index, row in enumerate(A):
        row.insert(0, b[index])
        temp_matrix.append(row)
    temp_matrix.insert(0, c)
    # initialize an empty transposed matrix
    m, n = len(A), len(A[0])
    temp_matrix_tr = [[0 for _ in range(n)] for _ in range(m)]
    # transpose the temporary matrix
    for i in range(m):
        for j in range(n):
            temp_matrix_tr[j][i] = temp_matrix[i][j]
    return temp_matrix, temp_matrix_tr


def print_matrix(M):
    for index, row in enumerate(M):
        print(row)


A = [[-1, -1], [-1, 1], [1, 2]]
b = [-3, -1, 2]
c = [1, 3]

temp, temp_tr = dualize(A, b, c)
print_matrix(temp)
print("#######")
print_matrix(temp_tr)
