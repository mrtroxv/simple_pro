import json
import Patterns
import config_st
import database_interaction
import User
import re 
from re import findall
database_file=open("database.txt","r+")
dict_n=json.load(database_file)


def logged_in():
    print("succes")

def log_in():
    print("login page")
def sign_up():
   
    print("=====signup page=====")

    def enter_ur_name():
     name=input("step1/4----enter ur full name ")
     i=0
     while(len(name)==0 or name==" ") :
         name=input("ur input is empety enter your name again")
        
         i=i+1
         if i==config_st.Max_input:
             fun()
     return name
            
    def enter_ur_birth_date():
     birth_date=input("step 2/4-----enter ur birth date")
     i=0
     while(len(birth_date)==0 or birth_date==" "):
         birth_date=input("ur input is empety enter your birthdate again")
        
         i=i+1
         if i==config_st.Max_input:
            fun()
     while(len(re.findall(Patterns.pattern_birthdate,birth_date))==0):
         birth_date=input("ur birth date is invalid enter ur birth date again")
     return birth_date
    def enter_ur_email():
     email=input("step 3/4-----enter ur email")
     i=0
     while(len(email)==0 or email==" "):
         email=input("ur input is empety enter your email again")
        
         i=i+1
         if i==config_st.Max_input:
             fun()
     for i in dict_n:
      if i==email:
         while(len(email)==0 or email==i):
             email=input("enter ur email")
     while(len(re.findall(Patterns.pattern_email,email))==0):
         email=input("ur email is invaled enter your email again")
     return email

        
    def enter_ur_password():
     password=input("step 4/4-----enter ur password")
     i=0

     while(len(password)==0):
         password=input("ur input is empety enter your password again")
        
         i=i+1
         if i==config_st.Max_input:
             fun()
     while(len(re.findall(Patterns.pattern_password,password))==0):
         password=input("ur password is invalid enter your password again")
     return password
    u=User.User(enter_ur_name(),enter_ur_birth_date(),enter_ur_email(),enter_ur_password())
    database_interaction.write(u)
    logged_in()
    
    


def fun():
 print ("----Home Page----\na.login\nb.signup\nc.exit")
 inp1=input("please select the charracter")
 if inp1=='a':
     log_in()
     fun()
 elif inp1=='b':
     sign_up()
     
 else:
     print("good bye")
fun()
exit()





 