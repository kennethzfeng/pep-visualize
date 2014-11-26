import unittest

from app import all_peps


class AppTest(unittest.TestCase):
    def setUp(self):
        self.test = 'Hello'

    def test_pep_number(self):
        self.assertEqual('Hello', self.test)

    def test_all_peps(self):
        valid_numbers = all_peps()
        self.assertIn(8, valid_numbers)
        self.assertNotIn(99, valid_numbers)


if __name__ == '__main__':
    unittest.main()
