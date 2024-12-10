s = "A man, a plan, a canal: Panama"
def is_valid_palindrome(s):
    s = s.lower()
    cleaned_text = ''
    for char in s:
        if char.isalpha():
            cleaned_text += char

    n = len(cleaned_text)

    left, right = 0, len(cleaned_text) - 1
    while left < right:
        # Step 3: Compare characters at left and right
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True
print(is_valid_palindrome(s))