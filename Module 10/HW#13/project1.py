#shift supervisor (1) salary (2) yearly bonus if production goals are met
#write ShiftSupervisor as a subclass of Employee 
#keep data attribute for annual salary, annual production bonus

import employee

def main():
    employee1 = employee.ShiftSupervisor('FN LN',1,80000,'yes')
    employee1.printInformation()

main()