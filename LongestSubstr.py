s = "abcabcbb"
output = []
word = ""
if s == "":
    print(0)
else:
    for char in s:
        if char in word:
            word = word[word.index(char) + 1:]
        word += char
        output.append(word)

    print(len(max(output, key=(len))))
    # print(len(max(output)))
