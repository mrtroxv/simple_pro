import User
import json
import hashlib
dict_n = {}
database_file = open("database.json", "r+")


def write(u):
    global dict_n
    global database_file
    dict_n = json.load(database_file)

    dict_n[u.email] = {"name": u.name, "birth_date": u.birth_date, "email": u.email,
                       "password": hashlib.md5(bytes(u.password, "utf-8")).hexdigest()}
    database_file.seek(0)
    json.dump(dict_n, database_file)
