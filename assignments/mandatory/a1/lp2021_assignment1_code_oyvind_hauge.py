#############################
#   NAME: ØYVIND HAUGE      #
#   PYTHON VERSION: 3.8.5   #
#############################


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
    # n += m
    return A, b, c, m, n


# 2.
def initial_tableau(A, b, c, m, n):
    alpha = []
    for row_idx, row in enumerate(A):
        new_row = [b[row_idx]]
        alpha.append(new_row)
        for col_idx in range(n):
            new_row.append(row[col_idx] * -1)
    x = [0] * n
    y = [] # TODO: ...
    z = [cc * xx for cc, xx in zip(c, x)]
    return alpha, c, x, y, z


def pivot_step(Alpha, c, x, y, i, k, l):
    pass


# Utility functions

def display_lp(A, b, c, m, n):
    for index, row in enumerate(A):
        print('\t'.join(map(str, row)) + ' [ %.2f ]' % (b[index]))


def display_tableau(A):
    for row_idx, row in enumerate(A):
        row_str = ''
        for col in row:
            row_str += '{:8.2f}'.format(col)
        print(row_str)


A = [[-1, 1], [1, 0], [0, 1]]

b = [1, 3, 2]

c = [1, 1]

m, n = 3, 2

A_new, b_new, c_new, m_new, n_new = transform(A, b, c, m, n)
A_new2, _, _, _, _ = initial_tableau(A_new, b_new, c_new, m_new, n_new)

display_tableau(A_new2)

# display_lp(A_new2, b_new, c_new2, m_new2, n_new2)
