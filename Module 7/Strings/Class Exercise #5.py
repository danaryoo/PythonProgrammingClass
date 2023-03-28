#Class Exercise #5
#This program counts the # of times the letter T (upper or lower) appears in a string
def main():
    count = 0 #create a variable to hold the counnt (variable must start with 0)
    my_string = input('Enter a sentence: ') #get a string from the user
    for ch in my_string: #count the Ts
        if ch == 'T' or ch == 't':
            count+= 1
    print(f'The letter T appears {count} times.') #print the result 

if __name__ == '__main__':
    main()