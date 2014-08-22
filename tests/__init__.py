import unittest


class PEPTest(unittest.TestCase):
    def setUp(self):
        self.test = 'Hello'

    def test_pep_number(self):
        self.assertEqual('Hello', self.test)


if __name__ == '__main__':
    unittest.main()
