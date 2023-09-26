import getpass

data = {'Minh':'012345','Skip':'45781'}
user_name = input("Enter your name:")
print('\n')
password = getpass.getpass("Enter your password :")

for user in data.keys():
    if user_name == user:
        while(password != data.get(user)):
            password = getpass.getpass("Enter Your Password Again : ")
        break
print("Verified")