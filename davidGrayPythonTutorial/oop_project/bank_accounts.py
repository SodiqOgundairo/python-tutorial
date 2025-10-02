class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmount, accName):
        self.balance = initialAmount
        self.name = accName
        print(
            f"\nAccount '{self.name}' created with balance \n${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance: {self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print(f"\nDeposit complete")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nInsufficient funds. Account '{self.name}' Current balance is ${self.balance:.2f}")

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print(f"\nWithdraw complete")
            self.getBalance()
        except BalanceException as e:
            print(f'\nWithdraw interrupted: {e}')

    def transfer(self, amount, destinationAccount):
        try:
            print('\n********** \n\nInitiating transfer...🚀')
            self.viableTransaction(amount)
            self.withdraw(amount)
            destinationAccount.deposit(amount)
            print(f"\nTransfer complete! ✅\n\n **********")
            # self.getBalance()
            # destinationAccount.getBalance()
        except BalanceException as e:
            print(f'\nTransfer interrupted. ❌ {e}')


class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance += amount * 1.05
        print('\nDeposit complete with 5% interest reward!')
        self.getBalance()


class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, accName):
        super().__init__(initialAmount, accName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount+self.fee)
            self.balance += amount * self.fee
            print('\nWithdraw completed.')
            self.getBalance()
        except BalanceException as e:
            print(f'\nWithdraw interrupted. ❌ {e}')
