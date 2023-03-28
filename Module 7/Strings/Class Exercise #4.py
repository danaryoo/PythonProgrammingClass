#Class Exercise #4
#This program reads test scores from a csv file + calculates each student's test average
def main():
    csv_file = open('test_scores.csv','r') #open the file
    lines = csv_file.readlines() #red the file's lines into a list
    csv_file.close() #close the file
    for line in lines: #process the lines
        tokens = line.split(',') #get the test scores as tokens
        total = 0.0 #calculate the total of the test scores
        for token in tokens:
            total += float(token)
        average = total / len(tokens)
        print(f'Average: {average}')

#execute the main function
if __name__ == '__main__':
    main()