import unittest
from src import Validate
password="Ahmad2000$"

class TestMyProject(unittest.TestCase):
    def test_name(self):
        self.assertFalse(Validate.is_validate_password(password),"is not valid")
 

if __name__ =="__main__":
    unittest.main()