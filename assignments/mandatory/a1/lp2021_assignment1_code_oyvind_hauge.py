#############################
#   NAME: ØYVIND HAUGE      #
#   PYTHON VERSION: 3.8.5   #
#############################


# assignment 1.1
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


# assignment 1.2
def initial_tableau(A, b, c, m, n):
    # populate matrix Alpha with NBVs
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


# assignment 1.3
def pivot_step(Alpha, c, x, y, i, l, k):
    # we'll increment pivot column index by one
    # because we only want to look at the variables
    i += 1  # FIXME: maybe increase x vector by one instead (to hold parameter as well as vars)
    # find the optimal pivot row
    j = optimal_pivot_row(Alpha, i)
    # divide values in pivot row with the
    # coefficient of the entering variable
    for col_index in range(k + 1):
        Alpha[j][col_index] /= abs(Alpha[j][i])
    # update all rows by adding values from pivot row
    for row_index in range(l):
        coeff = Alpha[row_index][i]
        # we don't want to update pivot row, so skip it.
        # Also, if value doesn't exist in the current row,
        # we want to skip it.
        if row_index == j or coeff == 0:
            continue
        for col_index in range(k + 1):
            updated_coeff = coeff * Alpha[j][col_index]
            if col_index == i:
                Alpha[row_index][col_index] = updated_coeff
            else:
                Alpha[row_index][col_index] += updated_coeff
    # update objective function
    coeff = c[i - 1]
    for col_index in range(k):
        if col_index == i - 1:
            c[col_index] = coeff * Alpha[j][col_index + 1]
        else:
            c[col_index] += coeff * Alpha[j][col_index + 1]
    # interchange new BV with new NBV
    x[i - 1], y[j] = y[j], x[i - 1]
    return Alpha, c, x, y


# Utility functions


def update_obj_function(row, i):
    pass


def optimal_pivot_row(Alpha, pivot_col):
    opt_value, opt_index = None, -1
    for index, row in enumerate(Alpha):
        if row[pivot_col] < 0:
            value = row[0] / abs(row[pivot_col])
            if opt_value is None or opt_value > value:
                opt_value = value
                opt_index = index
    return opt_index


def display_tableau(Alpha, c, x, y, z):
    # print all constraints
    for row_idx, row in enumerate(Alpha):
        row_str = 'x{0} ='.format(y[row_idx])
        for index, col in enumerate(row):
            if index > 0 and col == 0:
                row_str += '{0:<10}'.format('')
            else:
                row_str += '{:8.1f}'.format(col)
            if index > 0 and col != 0:
                row_str += 'x{0}'.format(x[index - 1])
        print(row_str)
    # print horizontal separator
    print('-' * 32)
    # print objective function
    row_str = 'ζ  ={0:8.1f}'.format(z)
    for param, var in zip(c, x):
        row_str += '{:8.1f}x{var}'.format(param, var=var)
    print(row_str + '\n')


A = [[-1, 1], [1, 0], [0, 1]]

b = [1, 3, 2]

c = [1, 1]

m, n = 3, 2

# LP in equational form
A_new, b_new, c_new, m_new, n_new = transform(A, b, c, m, n)

# initial simplex tableau
A_new2, c_new2, x, y, z = initial_tableau(A_new, b_new, c_new, m_new, n_new)

# print initial tableau
display_tableau(A_new2, c, x, y, z)

# do first pivot step
A_new3, c_new3, x_new, y_new = pivot_step(A_new2, c_new2, x, y, 1, m, n)

# print tableau after first pivot step
display_tableau(A_new3, c_new3, x_new, y_new, 0)


