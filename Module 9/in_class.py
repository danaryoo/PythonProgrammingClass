import Animal

def main():
    #puppy = Animal(4,2,'Bada')
    #print(puppy.GetName(), str(puppy.GetLeg()), str(puppy.GetAge()))
    
    cat = Animal()
    cat.GetName = input('what is the animal\'s name?: ')
    cat.GetLeg = input('how many legs does this animal have?: ')
    cat.GetAge = input('how old is the animal?: ')
    print(cat.GetName(), str(cat.GetLeg()), str(cat.GetAge()))

if __name__ == "__main__":
    main()