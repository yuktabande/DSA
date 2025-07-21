s = "aaabaaaa"
output = ''
if len(s) > 2:
    output = s[0]
    ptr = 1
    while ptr < len(s) - 1:
        if s[ptr] == s[ptr-1] and s[ptr] == s[ptr+1]:
            pass
        else:
            output += s[ptr]
        ptr += 1

    output += s[-1]
else:
    s = output
print(output)