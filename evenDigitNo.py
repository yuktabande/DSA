arr = [12, 345, 2, 6, 7896]
ans = 0 
for num in arr:
    count = 0
    while num > 0:
        count += 1
        num = int(num/10)
    if count % 2 == 0:
        ans += 1

print(ans)