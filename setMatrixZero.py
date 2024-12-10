matrix = [[0,1,2,0],
          [3,4,5,2],
          [1,3,1,5]]
rows = []
cols = []
          
print(matrix)
for i,row in enumerate(matrix): 
    for j,element in enumerate(row): 
        if element == 0:
            rows.append(i)
            cols.append(j)

# print(rows)
# print(cols)

# print(len(matrix[0]))
# print(len(matrix))
for b in cols:
    for a in range(0,len(matrix)):
        matrix[a][b] = 0 #[0,0] [1,0] [2,0] 
                         #[0,3] [1,3] [2,3]

for n in rows:
    for m in range(0,len(matrix[0])):
        matrix[n][m] = 0 #[0,0] [0,1] [0,2] [0,3]
                
print(matrix)