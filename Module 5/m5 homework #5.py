#Project #1
#user inputs actual value
#program outputs assessment value + property tax
def appraisal():
    real_value = float(input('How much is your property worth?: '))
    assessment_value = real_value * 0.60
    property_tax = (assessment_value / 100) * 0.72
    print (f'The assessment value is ${assessment_value:,.2f} and the property tax is ${property_tax:,.2f}')
    
appraisal()

#Project #2
#3 classes
#A = $20, B = $15, C = $10
#user inputs how much ticket is sold for each class
#program outputs total income

def income():
    classA = float(input('How many Class A tickets were sold? '))
    classB = float(input('How many Class B tickets were sold? '))
    classC = float(input('How many Class C tickets were sold? '))
    total = (classA*20) + (classB*15) + (classC*10)
    print(f'The total income is ${total:,.2f}')

income()

#Project #3
#state sales tax = 5%
#county sales tax = 2.5%
#user enters total sales for th  month
#program outputs (1) county sales tax (2) state sales tax (3) total sales tax (county + state)

def tax():
    sale = float(input('What was this month\'s total sale?: '))
    state_tax = sale * 0.05
    county_tax = sale * 0.025
    total_tax = state_tax + county_tax
    print(f'The state tax is ${state_tax:,.2f}. The county tax is ${county_tax:,.2f}. The total sales tax is ${total_tax:,.2f}')
    
tax()