i, j = 0, 0
mat = [[1,2,3],[4,5,6],[7,8,9]]
output = []
n, m = len(mat), len(mat[0])
direction = 1   # 1 = up-right, -1 = down-left

while len(output) < n * m:
    output.append(mat[i][j])
    
    if direction == 1:  # moving up-right
        if j == m - 1:      # right boundary → move down
            i += 1
            direction = -1
        elif i == 0:        # top boundary → move right
            j += 1
            direction = -1
        else:               # normal move
            i -= 1
            j += 1
    else:  # moving down-left
        if i == n - 1:      # bottom boundary → move right
            j += 1
            direction = 1
        elif j == 0:        # left boundary → move down
            i += 1
            direction = 1
        else:               # normal move
            i += 1
            j -= 1

print(output)