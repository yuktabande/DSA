def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n//2): #outer and inner layers
        for j in range(i, n-i - 1): #elements in layer
            #swap in cyclic manner 
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = temp
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
# n = len(matrix)
# print(n//2)
rotate_matrix(matrix)
print(matrix)