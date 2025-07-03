word = "a"
k = 10

next_letter = {"a":"b", "b":"c", "c":"d", "d":"e", "e":"f", "f":"g", "g":"h",
               "h":"i", "i":"j", "j":"k", "k":"l", "l":"m", "m":"n", "n":"o",
               "o":"p", "p":"q", "q":"r", "r":"s", "s":"t", "t":"u", "u":"v",
               "v":"w", "w":"x", "x":"y", "y":"z", "z":"a"}

while (len(word) < k):
    generated_str = ""
    for letter in word:
        generated_str += next_letter[letter]

    word += generated_str
print(word[k-1])