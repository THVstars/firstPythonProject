def is_palindrome(txt):
    return txt == txt[::-1]  # ::-1 reverses txt


print(is_palindrome("Taehyung"))
