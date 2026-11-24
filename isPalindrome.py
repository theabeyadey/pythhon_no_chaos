def reverse_word(text):
    reverse = ""
    for letter in text:
        reverse = letter + reverse
    return reverse

entered_text = input("Enter a word: ")

reversed_text = reverse_word(entered_text)

if reversed_text == entered_text:
    print(entered_text, "is a palindrome")
else:
    print(entered_text, "is not a palindrome")

