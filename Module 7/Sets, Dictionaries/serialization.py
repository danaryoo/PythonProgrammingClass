#Project #4 Serialization
#this program demonstrates object unpickling
import pickle

def main():
    end_of_file = False #to indicate end of file
    input_file = open('info.dat','rb') #open a file for binary reading
    while not end_of_file: #read to the end of the file
        try: 
            person = pickle.load(input_file) #unpickle the next object
            display_data(person) #display the object
        except EOFError:
            end_of_file = True #set the flag to indicate the end of the file has been reached
    input_file.close()

def display_data(): #displays the person data in the dictionary that is passed as an argument
    print('Name:', person['name'])
    print('Age:', person['age'])
    print('Weight:',person['weight'])
    print()

if __name__ == '__main__':
    main()
