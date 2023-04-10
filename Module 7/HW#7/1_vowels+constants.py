#1. Vowels and Constants
#user enters a string
print('This program returns the number of vowels and consonants in a sentence.')
user_str = str(input('Please enter a sentence: '))

def sounds():
    vowel_count = 0
    consonants_count = 0
    vowels = {'a','A','e','E','i','I','o','O','u','U'} #there probably is a better way to account for lower and uppercase
    consonants = {'b','B','c','C','d','D','f','F','j','J','k','K','m','M','n','N','p','P','q','Q','s','S','t','v','x','z'}
    for char in user_str:
        if char in vowels:
            vowel_count += 1
        else:
            consonants_count +=1
    return vowel_count, consonants_count

vowel_count, consonants_count = sounds()
print(f'The sentence contains {vowel_count} number of vowels and {consonants_count} number of consonants.')