import csv

def database():
  with open(r'C:\Users\dana.ryoo\Downloads\MBTI.csv','r',encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
      column1 = row[0]
      column2 = row[1]
      print(f'Column 1: {column1} | column 2: {column2}') 
  #csv_file = open(r'C:\Users\dana.ryoo\Downloads\\MBTI.csv','r')
  #createlist = csv_file.readlines()

database()