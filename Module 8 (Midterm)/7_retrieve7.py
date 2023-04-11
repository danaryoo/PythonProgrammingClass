#program creates a 2-D list with numbers 1- 10 + retrieves a lucky number 7
def retrieve7():
    OnetoTenList = [[1,2,3],
                    [4,5,6],
                    [7,8,9],
                    [10]]
    lucky7 = OnetoTenList[2][0]
    print(f'The lucky number is retrieved: {lucky7}')

retrieve7()