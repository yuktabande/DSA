matrix = [[1,2,3],[4,5,6],[7,8,9]]
sol = []
last_row = len(matrix)-1
last_col = len(matrix[0])-1
first_col = 0
first_row = 0

for i, row in enumerate(matrix):
    for j, element in enumerate(row):
        if i == first_row:
            if j != last_col: 
                sol.append(element)
                matrix[i][j] = None
            else:
                if i != last_row:
                    for m in range(0,(last_row-i)+1):
                        sol.append(matrix[i][m])
                    first_row += 1
                else:
                    if i != first_col:
                        sol.append(element)
                        matrix[i][j] = None
                    else: 
                        if j == first_col:
                            sol.append(element)
                            matrix[i][j] = None
                #last_col -= 1
                #last_row -= 1
                #first_col += 1
                #first_row += 1

print(sol)