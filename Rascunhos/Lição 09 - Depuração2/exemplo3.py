# Test

def is_square(matrix):
    for row in matrix:
        print row
        print len(row)
        print len(matrix)
        if len(row) != len(matrix):
            print ((("This is not a square matrix")))
            return False
        return True

a_matrix = [[1,0],
             [0,1],[0,1]]

print is_square(a_matrix)
