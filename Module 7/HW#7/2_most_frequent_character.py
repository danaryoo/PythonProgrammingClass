#user enters a statement
USER_INPUT = input('Enter a statement in lower case: ')

#program returns the character that appears the most frequently
each_count = {}

for letter in USER_INPUT:
    if letter.isalpha(): #check if the letters in the statement is a letter
        if letter in each_count: #if it is a letter 
            each_count[letter] +=1 #takes an account of each character + adds each time there 
        else:
            each_count[letter] = 1

frequent_character = None
highest_count = 0
for letter, count in each_count.items():
    if count > highest_count:
        frequent_character = letter
        highest_count = count

print(f'The most frequent character is "{frequent_character}" and it appears {highest_count} times.')