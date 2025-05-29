s = "1001"
i = 1
output = ""
while i < len(s):
    binary = s[i-1]+s[i]
    if binary == "00":
        output += 'A'
    elif binary == '01':
        output += 'T'
    elif binary == '10':
        output += 'C'
    elif binary == '11':
        output += 'G'
    i += 2
print(output)