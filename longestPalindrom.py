s = "abb"
left, right = 0, len(s)-1
output = ""
while left < right:
    if s[left] == s[right]:
        output += s[left]
    else:
        output = ""
    left += 1
    right -= 1
print(output)
rev = output[::1]
print(rev)
if right == left: 
    output += s[left] + rev
    #print(output)
else:
    output += rev

