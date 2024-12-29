def rotate_matrix(matrix):

    new_matrix=[]
    for col in zip(*matrix):
        print(list(col))
        new_matrix.append(list(reversed(col)))
    return new_matrix


matrix = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
rotated_matrix=rotate_matrix(matrix)
print(rotated_matrix)