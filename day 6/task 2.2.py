def palindrome(text):
    text = text.replace(" ", "").lower()

    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return palindrome(text[1:-1])


word = input("Text: ")

print(palindrome(word))