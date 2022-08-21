import unittest
from src import Validate
name="ahmad"

class TestMyProject(unittest.TestCase):
    def test_name(self):
        self.assertFalse(Validate.is_validate_name(name),"is not valid")
 

if __name__ =="__main__":
    unittest.main()