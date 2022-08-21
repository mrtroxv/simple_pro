import json
import hashlib
from src import DatabaseInteraction
database_file = open("src\database.json","r+")
if DatabaseInteraction.dict_n == {}:
    DatabaseInteraction.dict_n = json.load(database_file)


def is_valid(email, password):
    for i in DatabaseInteraction.dict_n:
        if i == email:
            if hashlib.md5(bytes(password, "utf-8")).hexdigest() == DatabaseInteraction.dict_n[i]["password"]:
                return True
            else:
                return False
    return False
