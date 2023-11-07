class User:
    def __init__(self,name,username,email):
        self.username = username
        self.name = name
        self.email = email
        print("User created!")
    def created_account(self):
        self.username = input()
        self.name = input()
        self.email = input()
    def introduce_yourself(self, guest_name):
        print("Hi {}, I'm {}! Contact me at {} .".format(guest_name, self.name, self.email))
    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)
    
    def __str__(self):
        return self.__repr__()
    
class UserDatabase:
    def __init__(self):
        self.users = []
    def insert(self, user):
        i = 0
        while i < len(self.users):
            # Find the first username greater than the new user's username
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)
    
    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user
    
    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email
        
    def list_all(self):
        return self.users
        
minh  = User("MinhTran","MINH","minh@email.com")
long  = User("LongHoang","LONG","long@email.com")
khanh = User("KhanhNguyen","KHANH","khanh@email.com")
mai   = User("MaiNguyen","MAI","mai@email.com")
tuan  = User("TuanTran","TUAN","tuan@email.com")
ngoc  = User("NgocMai","NGOC","ngoc@email.com")
users = [minh,long,khanh,mai,tuan,ngoc]
database = UserDatabase()
##database.insert(minh)
database.insert(minh)
database.insert(khanh)
database.insert(mai)


user = database.list_all()
guest = User(input(),input(),input())
database.insert(guest)
print(database)