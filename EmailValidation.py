import DatabaseInteraction
def email_check(email):
     for i in DatabaseInteraction.dict_n:
            if i == email:
                return True