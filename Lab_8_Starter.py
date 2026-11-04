# Name: Zoey Spies
# KUID: 3136594
# Lab session: Monday 11 AM
# Lab #8
# Description:
#   Compute the transitive closure of a zero-one matrix using Boolean matrix operations.
#
# Collaborators:
# Outside sources:

#This function is similar to Lab 3, but now it will keep running until the user inputs a square matrix
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
    #If blank line, try again
    if not x.strip():
        return get_square_matrix(ints=ints)

    items = x.replace(",", " ").split()
    length = len(items)
    matrix = []

    #Save the first row
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

    #Get the rest of the rows
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

#Maditory helper function to print a 2-D matrix
def print_matrix(M1, M2):
    print("Algorithm 1, Transitive Closure")
    for row in M1:
        for item in row:
            print(item, end=" ")
        print()
    print("Algorithm 2, Warshall Algorithm")
    for row in M2:
        for item in row:
            print(item, end=" ")
        print()
        
# ----------------- YOUR ADDED CODE BELOW -----------------
def transitive_closure(M):
    # Implement the transitive closure algorithm here
    for i in range(len(M)):
        for j in range(len(M)):
            if M[i][j] == 1:
                for k in range(len(M)):
                    if M[j][k] == 1:
                        M[i][k] = 1

def warshall(M):
    # Implement the Warshall algorithm here
    for i in range(len(M)):
        for j in range(len(M)):
            for k in range(len(M)):
                M[i][j] = M[i][j] or (M[i][k] and M[k][j])


def main():
    matrix = get_square_matrix(ints=True) #use this for both algorithms
    matrix1 = [row[:] for row in matrix]  # Create a copy of the matrix
    matrix2 = [row[:] for row in matrix]  # Create another copy of the matrix

    transitive_closure(matrix1)
    warshall(matrix2)
    print_matrix(matrix1, matrix2)

if __name__ == "__main__":
    main()
