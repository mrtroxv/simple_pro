import json
from logging import exception
import Patterns
import Session
import ConfigSt
import DatabaseInteraction
import User
import SessionMethod
import EmailValidation
import BirthdayProcess
import LoginValidation
import re
database_file = open("database.json", "r+")


def HomePage():
    print("----Home Page----\na.login\nb.signup\nc.exit")
    inp1 = input("please select the charracter: ")
    if inp1 == 'a':
        log_in()
    elif inp1 == 'b':
        try:
            sign_up()
        except:
            print("Error to many trial")
            HomePage()
    else:
        print("goood bye (!0^) ")
        exit()


def logged_in(email, password, name):
    print("          ----welcome page-----\n")
    print("name:", name, "-------------- email:", email, "\n")
    print("ur birth date :")
    BirthdayProcess.date_proc(email)
    print("\n")
    print("friends birthday reminder!")
    BirthdayProcess.fri_data_proc(email)
    print("\n")
    print("a.logout")
    print("b.exit")
    user_input = input("choose ur character")
    if user_input == "a":
        SessionMethod.clear()
        Session.s_write()
        HomePage()
    else:
        print("ur exit now (<!0!>)")
        exit()


def log_in():
    print("-----Login Page-----")

    def email_input():
        i = 0
        email = input("Please Enter ur Email")
        while len(email.strip()) == 0:
            if i == ConfigSt.MAX_INPUT:
                break
            email = input("enter ur email again!")
            i = i+1
        if i == ConfigSt.MAX_INPUT:
            HomePage()
        return email

    def password_input():
        i = 0
        password = input("Please Enter ur Password")
        while len(password.strip()) == 0:
            if i == ConfigSt.MAX_INPUT:
                break
            password = input("enter ur password again!")
            i = i+1
        if i == ConfigSt.MAX_INPUT:
            HomePage()
        return password
    j = 0
    while LoginValidation.is_valid(Session.email, Session.password) == False and j <= ConfigSt.MAX_INPUT:
        if j > 0:
            print("ur emial or password no vaild please try again")
        Session.email = email_input()
        Session.password = password_input()
        j = j+1

    if(j == ConfigSt.MAX_INPUT+1):
        SessionMethod.clear()
        HomePage()
    else:
        Session.name = DatabaseInteraction.dict_n[Session.email]["name"]
        Session.birthdate = DatabaseInteraction.dict_n[Session.email]["birth_date"]
        Session.s_write()
        logged_in(Session.email, Session.password, Session.name)


def sign_up():
    SessionMethod.clear()
    print("=====signup page=====")

    def enter_ur_name() -> str:
        name = input("step1/4----enter ur full name: ")
        i = 0
        while(len(name.strip()) == 0):
            if i == ConfigSt.MAX_INPUT:
                raise Exception("sorry'too much trials")
                break
            name = input("ur input is empety enter your name again")
            i = i+1

        return name
    ####################################################################

    def enter_ur_birth_date():
        birth_date = input("step 2/4-----enter ur birth date")
        i = 0
        while len(birth_date.strip()) == 0 or re.fullmatch(Patterns.pattern_birthdate, birth_date, flags=0) is None:
            if i == ConfigSt.MAX_INPUT:
                raise Exception(
                    "sorry'too much trials or birthdate not formated")
                break
            birth_date = input("ur input is empety enter your birthdate again")
            i = i+1

        return birth_date
        #####################################################################

    def enter_ur_email():
        email = input("step 3/4-----enter ur email")
        i = 0
        while(len(email.strip()) == 0 or re.findall(Patterns.pattern_email, email) is None or EmailValidation.email_check(email)):
            if i == ConfigSt.MAX_INPUT:
                raise Exception("Error to many trial or ur email is exist")
                break
            email = input(
                "ur input is empety or is exist  enter your email again: ")
            i = i+1
        return email
    #######################################################################

    def enter_ur_password():
        password = input("step 4/4-----enter ur password: ")
        i = 0
        while(len(password.strip()) == 0 or re.fullmatch(Patterns.pattern_password, password) is None):
            if i == ConfigSt.MAX_INPUT:
                raise Exception("password is not formated or empety")
                break
            password = input("ur input is empety enter your password again: ")
            i = i+1
        return password
        ########################################################################
    name = enter_ur_name()
    birth_date = enter_ur_birth_date()
    email = enter_ur_email()
    password = enter_ur_password()
    u = User.User(name, birth_date, email, password)
    DatabaseInteraction.write(u)
    SessionMethod.set(email, password, name, birth_date)
    logged_in(Session.email, Session.password, Session.name)


def main():
    dict_session = Session.s_read()
    if dict_session == {}:
        HomePage()
    else:
        logged_in(Session.email, Session.password, Session.name)


main()
