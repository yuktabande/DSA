num = 9669
max_num = num
list_num = list(str(num))
for i in range(len(list_num)):
    if list_num[i] == "9":
        list_num[i] = "6"
    else:
        list_num[i] = "9"
    number = int("".join(map(str, list_num)))
    max_num = max(max_num, number)
    if list_num[i] == "9":
        list_num[i] = "6"
    else:
        list_num[i] = "9"
    
print(max_num)
