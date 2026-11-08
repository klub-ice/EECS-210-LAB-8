# Name: Zoey Spies
# KUID: 3136594
# Lab session: Monday 11 AM
# Lab #8
# Description:
#   Compute the transitive closure of a zero-one matrix using Boolean matrix operations.
#
# Collaborators:
# Outside sources:

# This function is similar to Lab 3, but now it will keep running until the user inputs a square matrix
def get_square_matrix(ints=False):
    """
    Takes a square matrix of numbers from the user. Each row can be
    separated by commas and/or spaces. Automatically ends after the last row.

    If ints=False, the function returns a matrix of strings.
    If ints=True, they will be cast to int instead
    """
    print("Enter your matrix:")
    matrix = []

    x = input()
    # If blank line, try again
    if not x.strip():
        return get_square_matrix(ints=ints)

    items = x.replace(",", " ").split()
    length = len(items)
    matrix = []

    # Save the first row
    if not ints:
        matrix.append(items)
    else:
        try:
            row = [int(entry) for entry in items]
            matrix.append(row)
        except ValueError:
            print("Error: all entries must be numbers! Try again:")
            #If first row is bad, try again
            return get_square_matrix(ints=ints)

    # Get the rest of the rows
    while True:
        x = input()
        items = x.replace(",", " ").split()
        if len(items) != length:
            print("Error: row lengths are mismatched! Try again:")
            continue  # re-try the line
        if not ints:
            matrix.append(items)
        else:
            try:
                row = [int(entry) for entry in items]
                matrix.append(row)
            except ValueError:
                print("Error: all entries must be numbers! Try again:")
                continue  # re-try the line
        #Check if matrix has been completed (is square)
        if len(matrix) == length:
            return matrix

# Mandatory helper function to print a 2-D matrix
def print_matrix(m1, m2):
    print("Algorithm 1, Transitive Closure")
    for row in m1:
        for item in row:
            print(item, end=" ")
        print()
    print("Algorithm 2, Warshall Algorithm")
    for row in m2:
        for item in row:
            print(item, end=" ")
        print()

# ----------------- YOUR ADDED CODE BELOW -----------------
def boolean_product(a, b):
    """Boolean product of two n x n zero-one matrices."""
    n = len(a)
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if a[i][k] and b[k][j]:
                    c[i][j] = 1
    return c


def boolean_or(a, b):
    """Entrywise join of two n x n zero-one matrices."""
    n = len(a)
    return [[1 if (a[i][j] or b[i][j]) else 0 for j in range(n)] for i in range(n)]


def transitive_closure(m):
    # Algorithm 1: b = m ∨ m^[2] ∨ ... ∨ m^[n]
    n = len(m)
    a = [row[:] for row in m]
    b = [row[:] for row in m]
    for i in range(2, n + 1):
        a = boolean_product(a, m)
        b = boolean_or(b, a)
    return b


def warshall(m):
    # Algorithm 2: k (intermediate vertex) is the OUTER loop
    n = len(m)
    w = [row[:] for row in m]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                w[i][j] = 1 if (w[i][j] or (w[i][k] and w[k][j])) else 0
    return w


def main():
    matrix = get_square_matrix(ints=True)  # use this for both algorithms
    m1 = transitive_closure(matrix)
    m2 = warshall(matrix)
    print_matrix(m1, m2)


if __name__ == "__main__":
    main()