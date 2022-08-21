import json
email = ""
password = ""
name = ""
birthdate = ""
session_file = open("src\session.json", "r+")
dict_session = {}
dict_session_empty = {}


def s_write():
    if(email != ""):
        dict_session[0] = {"email": email, "password": password,
                           "name": name, "birthdate": birthdate}
        session_file.seek(0)
        json.dump(dict_session, session_file)
    else:
        session_file.seek(0)
        session_file.truncate(0)
        json.dump(dict_session_empty, session_file)


def s_read():
    session_file.seek(0)
    dict_session_n = json.load(session_file)
    dict_session = dict_session_n
    if dict_session!={}:
        global name
        name = dict_session['0']['name']
        global email
        email = dict_session['0']['email']
        global password
        password = dict_session['0']['password']
        global birthdate
        birthdate = dict_session['0']['birthdate']
        return dict_session
    else:
        return {}
            
