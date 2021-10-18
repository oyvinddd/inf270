###############################
##   NAME: ØYVIND HAUGE      ##
##   PYTHON VERSION: 3.8.5   ##
###############################


# assignment 1.1
def transform(A, b, c, m, n):
    # add slack vars to the end of each row
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
    # prepend c_0 to vector c (this is the initial objective value)
    c.insert(0, 0)
    z = c[0]
    return Alpha, c, x, y, z


# assignment 1.3
def pivot_step(Alpha, c, x, y, i, l, k):
    # assignment 1.6 (exit early if optimum was reached)
    if not any(coefficient > 0 for coefficient in c[1:]):
        return Alpha, c, x, y, False, True
    # assignment 1.4 & 1.5 (checking for degeneracy/unboundedness)
    j, unbounded = optimal_pivot_row(Alpha, i)
    if unbounded:
        return Alpha, c, x, y, True, False
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
    coeff = c[i]
    for col_index in range(k + 1):
        if col_index == i:
            c[col_index] = coeff * Alpha[j][col_index]
        else:
            c[col_index] += coeff * Alpha[j][col_index]
    # interchange new BV with new NBV
    x[i - 1], y[j] = y[j], x[i - 1]
    return Alpha, c, x, y, False, False


# assignment 1.7
def simplex_method(A, b, c, m, n):
    # maximum # of pivot steps for SM
    max_pivot_steps, step_count = calculate_max_steps(m, n), 0
    # transform LP from standard to equational form
    A_std, b_std, c_std, m_std, n_std = transform(A, b, c, m, n)
    # create the initial simplex tableau
    A, c, x, y, z = initial_tableau(A_std, b_std, c_std, m_std, n_std)
    # execute pivot steps until one of three conditions are met:
    #   1. unbounded/no optimal solution
    #   2. algorithm interrupted due to cycling
    #   3. an optimal solution was found
    while True:
        display_tableau(A, c, x, y)
        i = pick_pivot_column(c)
        A, c, x, y, unbounded, optimum_reached = pivot_step(A, c, x, y, i, m, n)
        if unbounded:
            print('The problem is unbounded/there is no optimal solution.')
            break
        if step_count > max_pivot_steps:
            print('Algorithm interrupted due to cycling.')
            break
        if optimum_reached:
            print('Found an optimal solution: {0} = {1}'.format(solution_vector(A, x, y), c[0]))
            break
        # keep track of how many steps we have taken
        step_count += 1


# Utility functions


def pick_pivot_column(c):
    for column_index, coefficient in enumerate(c):
        if column_index > 0 and coefficient > 0:
            return column_index
    return None


def optimal_pivot_row(Alpha, pivot_col):
    unbounded, degenerate_row = True, None
    opt_value, pivot_row = None, None
    for row_index, row in enumerate(Alpha):
        if row[pivot_col] < 0:
            # find the strictest constraint for the given variable
            current_value = row[0] / abs(row[pivot_col])
            # if the current value is 0, we have a degenerate pivot row
            # we should store it for later in case we don't find any better rows
            if current_value == 0:
                degenerate_row = row_index
            elif opt_value is None or opt_value > current_value:
                opt_value = current_value
                pivot_row = row_index
                unbounded = False
    # if we didn't find any good candidates for a pivot row
    # our last resort is to check if we found a degenerate
    # row that performs a degenerate pivot step.
    if pivot_row is None and degenerate_row is not None:
        pivot_row = degenerate_row
        unbounded = False
    return pivot_row, unbounded


def solution_vector(Alpha, x, y):
    d = {}
    for nbv in x:
        d[nbv - 1] = 0
    for row, bv in enumerate(y):
        d[bv - 1] = Alpha[row][0]
    return [d[key] for key in sorted(d.keys())]


def calculate_max_steps(m, n):
    # the number of basic feasible solutions puts an upper
    # bound on how many iterations the SM can have for a given LP
    return factorial(n + m) / (factorial(n) * factorial(m))


def factorial(n):
    n_fact = 1
    for i in range(1, n + 1):
        n_fact *= i
    return n_fact


def display_tableau(Alpha, c, x, y):
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
    row_str = 'ζ  ='
    for index, value in enumerate(c):
        if index == 0:
            row_str += '{:8.1f}'.format(value)
        else:
            if value == 0:
                row_str += '{0:<10}'.format('')
            else:
                row_str += '{:8.1f}x{var}'.format(value, var=x[index - 1])
    print(row_str + '\n')


'''
# feasible problem
A = [[-1, 1], [1, 0], [0, 1]]
b = [1, 3, 2]
c = [1, 1]
m, n = 3, 2
'''

# feasible problem 3 a)
A = [[1, 1], [1, 0], [0, 1]]
b = [5, 3, 4]
c = [1, 0]
m, n = 3, 2

'''
# feasible problem (bands & coils problem)
A = [[1/200, 1/140], [1, 0], [0, 1]]
b = [40, 6000, 4000]
c = [25, 30]
m, n = 3, 2
'''

'''
# unbounded problem
A = [[1, -1], [-1, 1]]
b = [1, 2]
c = [1, 0]
m, n = 2, 2
'''

'''
# requires degenerate step
A = [[-1, 1], [1, 0]]
b = [0, 2]
c = [0, 1]
m, n = 2, 2
'''

# run the simplex method on the above LP
simplex_method(A, b, c, m, n)