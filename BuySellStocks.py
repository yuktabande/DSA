prices = [3,3,5,0,0,3,1,4]
n = len(prices)
if n == 1:
    print(0)
max_ele = min_pos = max_pos = -1
diff = 0
for i in range(1, n):
    if prices[i] > max_ele or prices[i] == max_ele:
        max_ele 
    max_pos = i
    for j in range(0,i):
        min_ele = max_ele
        if prices[j] < min_ele:
            min_ele = prices[j]
        min_pos = j

        if max_pos == 0 or min_pos == max_pos:
            print(0)
        else:
            diff =  
