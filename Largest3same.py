num = "6777133339"
number = num[0]
counts = []
count = 0
for i in num:
    print(i,number)
    if i == number:
        count += 1
    else:
        number = i
        count = 1
    if count >= 3:
        counts.append(int(number))
output = ""
max_ele = max(counts)
output += (str(max_ele))*3
print(output)