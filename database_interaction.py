import USER
import json
import hashlib
def write(u):
 database_file=open("data_base.txt","r+")
 dict_n=json.load(database_file)
 
 dict_n[u.email]={"name":u.name,"birth_date":u.birth_date,"email":u.email,"password":hashlib.md5(bytes(u.password,"utf-8")).hexdigest()}
 database_file.seek(0)
 json.dump(dict_n,database_file)