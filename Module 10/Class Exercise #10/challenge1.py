class AnimalType:
    def eats(self):
        print('this animal likes to eat?')

class rabbits(AnimalType):
    def munch(self):
        print(' carrots ')

class birds(rabbits):
    def munch1(self):
        print('  seeds  ')

class dogs(AnimalType):
    def munch2(self):
        print('  dog food  ')

RabbitObject = rabbits()
RabbitObject.eats()
RabbitObject.munch()

#here we have the Bird Object inheriting from 2 different classes
BirdObject = AnimalType()
BirdObject = birds()

BirdObject.eats()
BirdObject.munch1()

#continue project #1(A), add 3rd animal + print screen the results
DogObject = dogs()
DogObject.eats()
DogObject.munch2()