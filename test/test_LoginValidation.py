import unittest
from src import LoginValidation
CorrectEmail="osama.hajqasem@hotmail.com"
CorrectPassword="Ahmad2000$"
WrongEmail="emad.hajqasem@hotmail.com"
WrongPassword="Ahmad3000$"
class TestMyProject(unittest.TestCase):
    def test_IsValid(self):
        self.assertTrue(LoginValidation.is_valid(CorrectEmail,CorrectPassword),"Is not valid")
    def test_IsValid(self):
        self.assertFalse(LoginValidation.is_valid(WrongEmail,WrongPassword),"Is  valid")
        


