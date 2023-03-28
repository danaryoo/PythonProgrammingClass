#Challenge exercise #4
import pickle
def total():
    numbers = [1,2,3,4,5,6,7,8,9,10]
    sum = 0
    for value in numbers:
        sum+=value #total the numbers in the list
    average = sum /len(numbers)
    print(f'the total is {sum}. The average is {average}')
    numbers_file = open('numbers.txt','wb')
    pickle.dump(numbers,numbers_file)
    numbers_file.close()
total()