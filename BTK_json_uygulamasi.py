import os                           #Terminal temizlemek için
os.system('cls||clear')

import json

class User:
    def __init__(self, username, password, email) -> None:
        self.username=username
        self.password=password
        self.email=email

class UserRepo:
    def __init__(self) -> None:
        self.users=[]
        self.isLoggedIn=False
        self.currentUser={}
        #Load users from .json file
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists('users.json'):
            with open('users.json','r',encoding='utf-8') as file:
                #uu=[  json.loads(u)  for u in json.load(file)]  #load ile jsondan çekilen string json bilgi python dict bilgiye dönüşüyor
                #print(uu)
                #self.users.append(User(u['username'],u['password'],u['email']))
                
                users=json.load(file) #load ile dosyadan json string bilgi çekiliyor
                for u in users:
                    u=json.loads(u) #Loads ile json bilgi python dict bilgiye dönüşüyor
                    #print(u)
                    newUser=User(u['username'],u['password'],u['email'])
                    self.users.append(newUser)
                    #print(u['username'])
            #print(self.users)


    def register(self, user:User):
        self.users.append(user)
        self.savetofile()
        print('Kullanıcı oluşturuldu.')

    def login(self,username,password):
        for u in self.users:
            if u.username==username and u.password==password:
                self.isLoggedIn=True
                self.currentUser=u
                print('login yapıldu.Username: ',self.currentUser.username)
                break

    def logout(self):
        self.isLoggedIn=False
        print(self.currentUser.username,' kişisinden çıkış yapıldı.')
        self.currentUser={}

    def identity(self):
        if self.isLoggedIn:
            print(f'Giriş yapılmış hesabın kullanıcı adı:{self.currentUser.username}')
        else:
            print('Giriş yapılmadı.')


    def savetofile(self):
        liste=[json.dumps(u.__dict__) for u in self.users]   #user verileri önce dict sonra json a çevrilip liste halinde kaydediliyor
        
        with open('users.json','w') as file:
            json.dump(liste , file) 

repo=UserRepo()

while True:
    print('Menü'.center(50,'*'))
    secim=input('1_-Register\n2-Login\n3-Logout\n4-Identity\nPress another key for EXİT\n')

    if secim=='1':
        username=input('Username: ')
        password=input('Password: ')
        email=input('Email: ')

        kullanici=User(username,password,email)
        repo.register(kullanici)


    elif secim=='2':
        name=input('Username: ')
        password=input('Password: ')
        repo.login(name,password)
    elif secim=='3':
        repo.logout()
    elif secim=='4':
        repo.identity()
    else:
        break #Exit





































