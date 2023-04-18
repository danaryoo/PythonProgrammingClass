import project5_BankAccount

def main():
    start_bal = float(input('enter the starting balance: '))
    savings = project5_BankAccount.BankAccount(start_bal)
    pay = float(input('how much were you paid this week?: '))
    print('will deposit that amount into your account')

    savings.deposit(pay)
    print(f'your account balance is ${savings.get_balance():,.2f}')

    cash = float(input('how much would you like to withdraw? '))
    print('will withdraw that amount into your account')

    savings.withdraw(cash)
    print(f'your account balance is ${savings.get_balance():,.2f}')

main()