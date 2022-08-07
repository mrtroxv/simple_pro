import User
import json
def write(u):
 database_file=open(".gitignore","r+")
 dict_n=json.load(database_file)
 
 dict_n[u.email]={"name":u.name,"birth_date":u.birth_date,"email":u.email,"password":hash(u.password)}
 database_file.seek(0)
 json.dump(dict_n,database_file)


#dict(name=u.name,birth_date=u.birth_date,email=u.email,password=hash(u.password))