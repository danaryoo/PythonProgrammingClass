#user enters a sentence where all of the words are run together but first character of each word is uppercase
#program separates the words by spaces + only the first word starts with an uppercase letter

USER_INPUT = str(input('Please enter a sentence where all of the words are run together but first character of each word is uppercase: '))

def separate_words(USER_INPUT):
    words = []
    current_word = ''
    
    for i, char in enumerate(USER_INPUT):
        if char.isupper() and i > 0:
            words.append(current_word)
            current_word = char.lower()
        else:
            current_word += char.lower()
    words.append(current_word)
    
    return ' '.join(words).capitalize()

formatted = separate_words(USER_INPUT)
print(formatted)