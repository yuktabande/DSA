nums = [1, 2, 3, 1]

pos1 = 0
for i in nums:
    pos2 = 0 
    for j in nums:
        if i == j and pos1 != pos2: 
            print("True")
        pos2 += 1
    pos1 += 1