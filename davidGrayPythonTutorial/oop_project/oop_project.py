from bank_accounts import *

Yemi = BankAccount(1000, "Yemi")
Tolu = BankAccount(2000, "Tolu")

Yemi.getBalance()
Tolu.getBalance()

Yemi.deposit(500)

Yemi.withdraw(10)
Tolu.transfer(20000, Yemi)
Tolu.transfer(20, Yemi)

Jim = InterestRewardsAcct(1000, 'Jim')
Jim.getBalance()
Jim.deposit(100)

Jim.transfer(100, Yemi)


Ope = SavingsAcct(1000, 'Ope')

Ope.getBalance()

Ope.deposit(100)

Ope.transfer(5000, Jim)
