def ss(number_list, n):
    found = False
    for i in number_list:
        if i == n:
            found = True
            break
    return found

numbers = range(0, 100)
s1 = ss(numbers, 2)
print(s1)
s2 = ss(numbers, 202)
print(s2)


def is_palindrome(word):
    word = word.lower()
    return word[::-1] == word


print(is_palindrome("Mother"))
print(is_palindrome("Mom"))
