import unittest
from src import Validate
email="wafa.hajqasem@hotmail.com"

class TestMyProject(unittest.TestCase):
    def test_email(self):
        self.assertFalse(Validate.is_validate_email(email),"is not valid")
 

if __name__ =="__main__":
    unittest.main()