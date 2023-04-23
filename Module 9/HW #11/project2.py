import project2_Employee

def main():
    name = (input('enter the name: '))
    id = (input('enter the id: '))
    department = (input('enter the department: '))
    title = (input('enter the job title: '))

    v1 = project2_Employee.Employee.set_name = name
    v2 = project2_Employee.Employee.set_id = id
    v3 = project2_Employee.Employee.set_department = department
    v4 = project2_Employee.Employee.set_title = title

    print(f'Name {v1}      ID Number {v2}      Department {v3}      Job Title {v4}')

main()