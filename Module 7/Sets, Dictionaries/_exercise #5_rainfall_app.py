#Challenge Exercise #5
#this program will ask for the monthly rainfall to get the total and store it in a list
def total(numbers):
    sum = 0
    for value in numbers:
        sum+= value
    return sum

def main():
    month_of_the_year = ['January','February','March','April','May','June','July','August','September','October','November','December']
    monthly_rain = []
    
    print('Enter the rain fall for each month.\n')

    index = 0
    for i in month_of_the_year:
        rain = float(input(f'Enter the amount of rain for {i}: '))
        monthly_rain.insert(index,rain)
        index+=1
    
    total_rain = total(monthly_rain)
    average_rain = total_rain/len(monthly_rain)
    less_rain = min(monthly_rain)
    less_rain_index = monthly_rain.index(less_rain)
    most_rain = max(monthly_rain)
    most_rain_index = monthly_rain.index(most_rain)

    print(f'The total rain in the year was: {total_rain}')
    print(f'The average rain in the year was: {average_rain}')
    print(f'The month with the lowest rain was {month_of_the_year[less_rain_index]} with {less_rain} inches of rain')
    print(f'The month with the most rain was {month_of_the_year[most_rain_index]} with {most_rain} inches of rain')

    write('yearly_rain.txt', monthly_rain, total_rain, month_of_the_year)


def write(name, monthly_rain, total, month_of_the_year):
    index = 0
    output =open(name,'w')
    for rain in monthly_rain:
        output.writelines(f'{month_of_the_year[index]}: {rain} inches\n')
        index+=1
    output.writelines(f'The total rain: {total:.2f} inches\n')
    output.writelines(f'The average rain on this year was {total/len(month_of_the_year)} inches\n')
    less_rain = min(monthly_rain)
    less_rain_index = monthly_rain.index(less_rain)
    most_rain = max(monthly_rain)
    most_rain_index = monthly_rain.index(most_rain)    
    output.writelines(f'The month with the lowest rain was {month_of_the_year[less_rain_index]} with {less_rain} inches of rain\n')
    output.writelines(f'The month with the most rain was {month_of_the_year[most_rain_index]} with {most_rain} inches of rain\n')

total()
main()
write()
