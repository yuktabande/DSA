s = "anagram"
t = "nagaram"

s_count = {}
t_count = {}
for char in s:
    if char.isalpha():
        s_count[char] = s_count.get(char, 0) + 1
for char in t:
    if char.isalpha():
        t_count[char] = t_count.get(char,0) + 1

if s_count == t_count:
    print(True)