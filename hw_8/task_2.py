def is_palindrome(text):
    cleaned_chars = []
    for val in text:

        if val.isalpha() or val.isdigit():
            cleaned_chars.append(val.lower())
    cleaned_text = ''.join(cleaned_chars)
    return cleaned_text == cleaned_text[::-1]


assert is_palindrome('A man, a plan, a canal:!№";";"%"%"%"%"% Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
