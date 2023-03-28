#Class Exercise #3
#This program demostrates how to tokenize strings

def main():
    #strings to tokenize
    str1 = 'one two three four'
    str2 = '10:20:30:40:50'
    str3 = 'a/b/c/d/e/f'
    #display the token in each string
    display_tokens(str1,' ')
    print()
    display_tokens(str2, ':')
    print()
    display_tokens(str3,'/')

def display_tokens(data, delimiter):
    tokens = data.split(delimiter)
    for item in tokens:
        print(f'Token: {item}')

#execute the main function
if __name__ == '__main__':
    main()