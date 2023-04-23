#program creates an object of the class + prompts the user to enter the name, type, age of his/her pet
#display the data

import project1_Pet

def main():
    name = (input('enter the name '))
    animal_type = (input('enter the pet\'s type '))
    age = (input('enter the age '))

    v1 = project1_Pet.Pet.set_name = name
    v2 = project1_Pet.Pet.set_animal_type = animal_type
    v3 = project1_Pet.Pet.set_age = age


    print(f'Your pet\'s name is {v1} and the type is {v2}.\nIt is {v3} years old.')

main()