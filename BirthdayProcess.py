import json
import DateCalculation
import DateCalculationFrinde
import Session
database_file = open("database.json", "r+")
birt_date = ""
fri_dict = {}
sorted_dict = []
dict_n = json.load(database_file)


def date_proc(email):
    DateCalculation.calculate_day(Session.birthdate)


def fri_data_proc(email):
    for i in dict_n:
        if i != email:
            fri_dict[DateCalculationFrinde.calculate_day(dict_n[i]["birth_date"])] = {
                "name": dict_n[i]["name"], "birthday": DateCalculationFrinde.calculate_day(dict_n[i]["birth_date"])}
    sorted_dict = sorted(fri_dict)
    i = 0
    null = True
    if len(sorted_dict) != 0:
        while i < len(sorted_dict):
            if sorted_dict[i] < 7:
                null = False
                print(fri_dict[sorted_dict[i]]["name"], end=" ")
                if fri_dict[sorted_dict[i]]["birthday"] == 0:
                    print("today")
                else:
                    print("reminde ",
                          fri_dict[sorted_dict[i]]["birthday"], "day")

            i = i+1
    if null:
        print("empty")
