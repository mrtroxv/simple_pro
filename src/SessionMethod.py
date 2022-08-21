from src import Session
def clear():
    Session.email = ""
    Session.password = ""
    Session.birthdate = ""
    Session.name = ""
def set (email,password,name,birth_date):
     Session.email = email
     Session.password = password
     Session.name = name
     Session.birthdate = birth_date
