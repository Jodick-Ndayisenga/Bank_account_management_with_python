class Bank_Account:
    def __init__(self):
        name = str(input('What is your name: '))
        self.name = name
        self.balance = 0
        self.cutomers = []
        if self.name not in self.cutomers:
            self.cutomers.append(self.name)

    def deposit(self):
        amount= float(input('Enter the amount you want to deposit: '))
        self.balance += amount
        print(f'Thank you! \nThe amount of {amount} has successfully been deposited on your account!')


    def withdraw(self):
        amount = float(input('Enter the amount of money you want to withdraw: '))
        if self.balance >= amount:
            self.balance -= amount
            print(f'Thank you! \nThe Amount of {amount} has successfully be transacted!!\nThe new balance is {self.balance}')

        else:
            print('Sorry your balance is not enough for such transaction!!\nPlease, Recharge your account.')


    def display(self):
        print(f'Your net balance is {self.balance}')

custo = Bank_Account()
print('')
custo.deposit()
print('')
custo.withdraw()
print('')
choice = input('Type yes if you want to see all the bank account information: ')
if choice != 'yes':
    print('Thank you for using our services!!')
    quit()
else:
    print(custo.name)
    custo.display()
