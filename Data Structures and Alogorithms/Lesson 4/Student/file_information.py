from os import *

class Account():
    def __init__(self,name,password):
        self.name     = name
        self.password = password
    def createdAccount(self):
        self.name     = input("Your account'name:")
        self.password = input("Your account'password:")
        repeat_password = input("Repeat your account'password:")
        if repeat_password != self.password:
            print("Can't created account!")
            return self.createdAccount()
        else:
            print("User created!")
    def __repr__(self):
        return "Account(name='{}', password='{}')".format(self.name, self.password)
    def __str__(self):
        return self.__repr__()

class DatabaseUser():
    def __init__(self) -> None:
        self.user = []
    def insert(self, user):
        i = 0
        while i < len(self.users):
            # Find the first username greater than the new user's username
            if self.users[i].name > user.name:
                break
            i += 1
        self.users.insert(i, user)
    
database = []
Admin = Account('Admin','xbox360@email')
new_account = Admin.createdAccount()
print(new_account)
database = database.append(new_account)
