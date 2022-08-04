import json
from re import A
import re

database_file=open("database.txt","r+")
dict_n=json.load(database_file)
def loged_in():
    print("succes")

def login():
    print("login page")
    return
def signup():
    pattern1="\w{1,}.\w{1,}@\w{1,}.com"
    pattern2="^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
    print("signup page")
    name=input("enter ur full name ")
    i=0
    while(len(name)==0):
        name=input("re enter ur name")
        
        i=i+1
        if i==2:
            exit()
    birth_date=input("enter ur birth date")
    i=0
    while(len(birth_date)==0):
        birth_date=input("re enter ur birth_date")
        
        i=i+1
        if i==2:
            exit()
    email=input("enter ur email")
    i=0
    while(len(email)==0):
        email=input("re enter ur email")
        
        i=i+1
        if i==2:
            exit()
    for i in dict_n:
     if i==email:
        while(len(email)==0 or email==i):
            email=input("enter ur email")
    while(len(re.findall(pattern1,email))==0):
        email=input("enter your email again")

        
    
    password=input("enter ur password")
    i=0

    while(len(password)==0):
        password=input("re enter ur password")
        
        i=i+1
        if i==2:
            exit()
    while(len(re.findall(pattern2,password))==0):
        password=input("enter your password again")
    
    u=User(name,birth_date,email,password)
    dict_n[email]=dict(name=u.name,birth_date=u.birth_date,email=u.email,password=hash(u.password))
    database_file.seek(0)
    json.dump(dict_n,database_file)
    loged_in()

class User:
    def __init__(self,name,birth_date,email,password):
        self.name=name
        self.birth_date=birth_date
        self.email=email
        self.password=password
def fun():
 print ("----Home Page----\na.login\nb.signup\nc.exit")
 inp1=input("please select the charracter")
 if inp1=='a':
     login()
     fun()
 elif inp1=='b':
     signup()
     
 else:
     print("good bye")
fun()
exit()





 