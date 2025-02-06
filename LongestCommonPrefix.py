strs = ["flower", "flow", "flight"]
if not strs:
    print("")
    exit()

prefix = strs[0]
for word in strs[1:]:
    while not word.startswith(prefix):
        prefix = prefix[:-1]
        if not prefix:
            break
print(prefix)