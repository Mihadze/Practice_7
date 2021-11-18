def is_palindrome(s):
    while len(s) > 1:
        if s[0] == s[-1]:
            s = s[1:-1]
            return is_palindrome(s)
        else:
            return False
    return True
