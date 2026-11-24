def count_vowels(text):
    number_of_vowels = 0
    vowel_sample = 'aeiou'

    for letter in text.lower():
        if letter in vowel_sample:
            number_of_vowels += 1
            
    return number_of_vowels

def count_consonants(text):
    number_of_consonants = 0
    vowel_sample = 'aeiou'

    for letter in text.lower():
        if letter.isalpha() and letter not in vowel_sample:
            number_of_consonants += 1
            
    return number_of_consonants

entered_text = input("Enter a word: ")
print(f"Number of vowels is {count_vowels(entered_text)}")
print(f"Number of consonants is {count_consonants(entered_text)}")

