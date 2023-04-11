#user inputs number of fat, carbohydrate (grams) per day
#program calculates calories from fat (fat grams * 9) and carb (carbs * 4)

def calories_counter():
    user_fat = int(input('Please enter the amount of fat (in grams): '))
    user_carb = int(input('Please enter the amount of carbohydrates (in grams): '))
    fat = user_fat * 9
    carb = user_carb * 4
    print(f'You have consumed {fat} calories from fat and {carb} calories from carbohydrates.')

calories_counter()