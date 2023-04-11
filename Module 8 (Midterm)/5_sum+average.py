#program has a list of numbers 20 - 30 & sums and averages the numbers

def sum_average():
    TwentytoThirtyList = [20,21,22,23,24,25,26,27,28,29,30]
    sum = 0
    average = 0
    for number in TwentytoThirtyList:
        sum+=number
        average = sum/len(TwentytoThirtyList)
    print(f'The total is {sum} and the average is {average:,.1f}.')
    

sum_average()