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
    return A, b, c, m, n


# 2.
def initial_tableau(A, b, c, m, n):
    Alpha = []
    for row_idx, row in enumerate(A):
        new_row = [b[row_idx]]
        Alpha.append(new_row)
        for col_idx in range(n):
            new_row.append(row[col_idx] * -1)
    # there are (n + m) variables in total
    # now populate the vectors x and y
    x, y = [], []
    for i in range(m + n):
        var_num = i + 1
        if i < n:
            x.append(var_num)
        else:
            y.append(var_num)
    # objective value is initially set to 0
    z = 0
    return Alpha, c, x, y, z


def pivot_step(Alpha, c, x, y, i, k, l):
    # 1. find the optimal pivot row
    j = optimal_pivot_row(Alpha, i)
    # 2. swap NBV (right-hand side) with BV (left-hand side)
    # 3.


# Utility functions


def optimal_pivot_col(c):
    opt_value, opt_index = 0, -1
    for index, value in enumerate(c):
        if value > opt_value:
            opt_value = value
            opt_index = index
    return opt_index


def optimal_pivot_row(Alpha, pivot_col):
    opt_value, opt_index = None, -1
    # skip constant in the first column of A
    pivot_col = pivot_col + 1
    for index, row in enumerate(Alpha):
        if row[pivot_col] < 0:
            value = row[0] / abs(row[pivot_col])
            if opt_value is None or opt_value > value:
                opt_value = value
                opt_index = index
    return opt_index


def display_tableau(Alpha, c, x, y):
    # print all constraints
    for row_idx, row in enumerate(Alpha):
        row_str = 'x{0} ='.format(y[row_idx])
        for index, col in enumerate(row):
            row_str += '{:8.1f}'.format(col)
            if index > 0:
                row_str += 'x{0}'.format(x[index - 1])
        print(row_str)
    # print horizontal separator
    print('-' * 32)
    # print objective function
    row_str = '{0: <12}'.format("S  =")
    for param, var in zip(c, x):
        row_str += '{:8.1f}x{var}'.format(param, var=var)
    print(row_str)


A = [[-1, 1], [1, 0], [0, 1]]

b = [1, 3, 2]

c = [1, 1]

m, n = 3, 2

# LP in equational form
A_new, b_new, c_new, m_new, n_new = transform(A, b, c, m, n)

# initial simplex tableau
A_new2, c_new2, x, y, z = initial_tableau(A_new, b_new, c_new, m_new, n_new)

#pivot_step(A, c_new2, x, y, 0, m, n)

display_tableau(A_new2, c, x, y)

