from bank_accounts import *

Minh = BankAccount(1000,'Minh')
Nam = BankAccount(2000,'Nam')

Minh.getBalance()
Nam.getBalance()

Nam.deposit(10000)

Nam.withDraw(1000)
Minh.withDraw(20000)

Minh.transfer(1000,Nam)