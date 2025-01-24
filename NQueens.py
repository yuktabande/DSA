N = 4 
matrix = [[0 for _ in range(N)] for _ in range(N)]
sol = []
for i,row in enumerate(matrix):
    for j,num in enumerate(row):
        Q = (i,j)
        for k,sol_row in enumerate(sol):
            for l,num in enumerate(sol_row):
                if i!=k and j!=l and j+1 != l and j-1 != l:
                    sol.append((i,j))
print(sol)
                 
