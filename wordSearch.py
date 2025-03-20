def exist(board, word):
    rows, cols = len(board), len(board[0])
    
    def dfs(r, c, index):
        if index == len(word):  # If we matched all letters
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
            return False
        
        # Mark the cell as visited by replacing it temporarily
        temp = board[r][c]
        board[r][c] = "#"  # Mark as visited
        
        # Explore in four directions: right, left, down, up
        found = (dfs(r+1, c, index+1) or 
                 dfs(r-1, c, index+1) or 
                 dfs(r, c+1, index+1) or 
                 dfs(r, c-1, index+1))
        
        # Restore the cell
        board[r][c] = temp
        return found
    
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == word[0] and dfs(i, j, 0):  # Start DFS if first letter matches
                return True
    
    return False

# Example Usage
board = [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]]

word = "ABCCED"
print(exist(board, word))  # Output: True
