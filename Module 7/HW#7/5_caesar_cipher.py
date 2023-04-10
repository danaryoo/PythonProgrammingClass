#Caesar Cipher = replace each letter with a letter a certain number of spaces up the alphabet 
#user inputs a statement + shift amount
#program returns the Caesar Cipher'd statement

user_input = str(input('Please enter a statement to be Caesar Ciphered (all lowercase): '))
new_position = int(input('What is the shift amount? (1-26): '))

def caesar_cipher(user_input,new_position):
    cipher = [chr(i) for i in range(97,123)] #ASCII lowercase letter numbered range
    characters = list(user_input)
    for i in range(len(characters)):
        if characters[i] in cipher:
            index = cipher.index(characters[i])
            new_index = (index + new_position) % 26 #setting the new order
            characters[i] = cipher[new_index]
    return ' '.join(characters)

caeser_message = caesar_cipher(user_input,new_position)
print(caeser_message)