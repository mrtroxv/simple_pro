from src import Patterns
import re
from src import EmailValidation


def is_validate_bithdate(birth_date):
    return len(birth_date.strip()) == 0 or re.fullmatch(Patterns.pattern_birthdate, birth_date, flags=0) is None
def is_validate_name(name):
    return len(name.strip()) == 0
def is_validate_email(email):
    return len(email.strip()) == 0 or re.fullmatch(Patterns.pattern_email, email) is None or EmailValidation.email_check(email)
def is_validate_password(password):
   return len(password.strip()) == 0 or re.fullmatch(Patterns.pattern_password, password) is None

