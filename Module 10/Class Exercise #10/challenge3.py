import vehicles

def main():
    used_car = vehicles.Automobiles('Audi',2022,45000,80000.0)
    
    print('Make: ' + used_car.get_make())
    print('Model: '+ str(used_car.get_model()))
    print('Mileage: '+ str(used_car.get_mileage()))
    print('Price: '+ str(used_car.get_price()))

    used_car2 = vehicles.Car_demo('Honda',2022,45000,80000)
    used_car2.print_description()

main()
