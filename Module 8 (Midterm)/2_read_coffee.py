def read_coffee():
    infile = open('coffee.txt','r')
    fileContents = infile.read()
    infile.close()
    print(fileContents)

read_coffee()