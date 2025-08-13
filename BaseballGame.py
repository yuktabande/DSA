output = []
operations = ["1","C","-62","-45","-68"]

for i in operations:
    if i == '+':
        num1 = int(output[-1])
        num2 = int(output[-2])
        output.append(num1+num2)
    elif i == 'D':
        num = int(output[-1])
        output.append(num*2)
    elif i == 'C':
        output.pop(-1)
    else:
        output.append(int(i))
print(sum(output))


