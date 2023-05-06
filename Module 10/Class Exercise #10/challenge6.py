#continue challenge3_Vehicles.py and add electronic vehicle car with same description
import vehicles

def main():
    used_car = vehicles.Car_demo('Audi',2022,45000,80000.0,4,'no')
    used_car2 = vehicles.Car_demo('Honda',2022,45000,80000,2,'no')
    used_car3 = vehicles.Car_demo('Kia',2022,50000,65000,4,'yes')
    used_car.print_description()
    used_car2.print_description()
    used_car3.print_description()

main()
