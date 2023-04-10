#pig latin = removes the first letter and place that letter at the end of the word + add 'ay' in the end
print('This program converts your statement into Pig Latin')
USER_STAT = str(input('Please enter your statement (the statement will be converted to uppercase): '))

def pig_latin():
    user_converted = USER_STAT.upper()
    each_word = user_converted.split()
    converted = []
    for word in each_word:
        converted = converted + [word[1:]+ word[0] + 'AY']
    finished = ' '.join(converted)
    return finished

print(pig_latin())