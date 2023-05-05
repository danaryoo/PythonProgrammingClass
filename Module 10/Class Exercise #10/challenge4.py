#continue from challenge3, add the # of doors for each car
#include mutator and accessor
import vehicles

def main():
    used_car = vehicles.Car_demo('Audi',2022,45000,80000.0,4)
    used_car2 = vehicles.Car_demo('Honda',2022,45000,80000,2)
    used_car.print_description()
    used_car2.print_description()

main()
