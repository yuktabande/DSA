# stack = []
# stack.append(1)
# stack.append(2)
# top = stack.pop()
# print(stack)

##RULES 
#"/home/" = "/home" : should not end with slash
#"/home//foo/" = "/home/foo": multiple slashes replaced by 1
#"/home/user/Documents/../Pictures" = "/home/user/Pictures"
#"/../" = "/"
#"/.../a/../b/c/../d/./" = "/.../b/d"


stack = []
cur = ""
for c in path + "/":
    if c == "/":
        if cur == "..":
            if stack: stack.pop()
        elif cur != "" and cur!= ".":
            stack.append(cur)
        cur = ""
    else:
        cur += c

print("/"+"/".join(stack))
