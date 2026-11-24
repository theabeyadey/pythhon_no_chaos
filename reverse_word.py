def reverse_word(text):
    reverse =""
    for letter in text:
        reverse = letter + reverse
        
    return reverse

entered_text = input("Enter a word: ")
print(reverse_word(entered_text))
