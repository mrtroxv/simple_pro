import json
import hashlib
from pickle import FALSE
database_file=open("data_base.txt","r+")
dict_n=json.load(database_file)
def is_valid(email,password):
    for i in dict_n:
        if i==email:
            if hashlib.md5(bytes(password,"utf-8")).hexdigest()==dict_n[i]["password"]:
                return True
            else:
                return False
    return False
                        