#given an array; to check if the string exists, vertically or horizontally adj
#for i in range 
#   for j in range 
#       if array[i][j] == string's 1st letter:
#           for letter in string in range 1,n:
#               if letter is not array[i+1][j] or array[i][j+1]:
#                   return false
#           return true


board = [["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]]

word = "ABCCED"
total_elements = sum(len(row) for row in board)
for i in range(0, len(board[0]+1)):
    for j in range(i, len(board[0]+1)):
        if board[i][j] == word[0]:
            for letter in word:
                if letter != board[i+1][j] or letter != board[i][j+1]:
                    print("False")
            print("True")
#