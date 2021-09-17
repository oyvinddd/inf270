#############################
#   NAME: ØYVIND HAUGE      #
#   PYTHON VERSION: 3.8.5   #
#############################

# Utility functions

def display_lp(A, b, c, m, n):
    for index, row in enumerate(A):
        print('\t'.join(map(str, row)) + ' [ %.2f ]' % (b[index]))

# 1.
def transform(A, b, c, m, n):
    # add slack vars to the end of each row
    # and increase n with # of slack vars
    for row_idx, row in enumerate(A):
        for idx in range(m):
            if idx == row_idx:
                row.append(1)
            else:
                row.append(0)
    #n += m
    return A, b, c, m, n

# 2.
def initial_tableau(A, b, c, m, n):
    Alpha = []
    for row_idx in range(m):
        row = [b[m]]


    #for row_idx, row in enumerate(A):
    #    # change the sign of all NBVs
    #    [x * -1 for x in row]
        # add intial values
    #    row.insert(0, b[row_idx])
    return Alpha, c, m, n

A = [[-1, 1], [1, 0], [0, 1]]

b = [1, 3, 2]

c = [1, 1]

m, n = 3, 2

A_new, b_new, c_new, m_new, n_new = transform(A, b, c, m, n)
A_new2, c_new2, m_new2, n_new2 = initial_tableau(A_new, b_new, c_new, m_new, n_new)

display_lp(A_new2, b_new, c_new2, m_new2, n_new2)
