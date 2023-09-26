class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, accName):
        self.balance = initialAmount
        self.name = accName
        print(f"\nAccount {self.name} created.\n Balance = ${self.balance:.2f}")
    
    def getBalance(self):
        print(f"\nAccount {self.name} balance = {self.balance:.2f} $")
        
    def deposit(self, amount):
        self.balance += amount
        print(f"\nDeposit complete.")
        self.getBalance()
    
    def viableTransaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account {self.name} only has a balance of ${self.balance:.2f}"
            )
    
    def withDraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print("\nWithdraw complete!")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')
            
    def transfer(self,amount, account):
        try:
            print('\n***********\nBeginning transfer..')
            self.viableTransaction(amount)
            self.withDraw(amount)
            account.deposit(amount)
            print('\nTransfer complete!')
        except BalanceException as error:
            print('\nTransfer interrupted!')