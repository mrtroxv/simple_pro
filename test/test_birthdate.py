import unittest
from src import Validate
birth_date="02/05/2000"

class TestMyProject(unittest.TestCase):
    def test_birthdate(self):
        self.assertFalse(Validate.is_validate_bithdate(birth_date),"is not valid")
