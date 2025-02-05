s = "()"

# stack.append(1)
# stack.append(2)
# print(stack.pop()) #2
# print(stack)#1
def validParentheses(s):
    stack = []
    pairs = {")": "(","}": "{", "]":"["}
    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
    return not stack
    validParentheses(s)