def is_palindrome(word):
    for i in range(len(word)//2):
        if word[i] != word[len(word)-i-1]:
            return False
    return True

def is_palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])

def is_palindrome(word):
    length = len(word)
    for i in range(length // 2):
        if word[i] != word[length - i - 1]:
            return False
    return True
