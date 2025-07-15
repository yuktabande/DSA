word = "22aN"

vowels = ["a","A","e","E","i","I","o","O","u","U"]
consonants = ["b","B","c","C","d","D","f","F","g","G","h","H","j","J","k","K","l","L","m","M","n","N","p","P","q","Q","r","R","s","S","t","T","v","V","w","W","x","X","y","Y","z","Z"]
number = ["0","1","2","3","4","5","6","7","8","9"]
vowelcheck = 0
consonantcheck = 0
numcheck = 0
char_length = 0
for char in word:
    if char in vowels:
        vowelcheck += 1
        char_length += 1
    elif char in consonants:
        consonantcheck += 1
        char_length += 1
    elif char in number:
        numcheck += 1
print(char_length)
if (numcheck+vowelcheck+consonantcheck) == len(word) and len(word) > 2 and consonantcheck > 0 and vowelcheck> 0:
    print(True)
else:
    print(False)