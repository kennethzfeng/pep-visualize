import unittest
from app.models import PEP


class PEPTest(unittest.TestCase):
    def setUp(self):
        path = 'pep_documents/pep-0008.txt'
        with open(path, 'rb') as f:
            data = f.read()
        self.pep = PEP(data)

    def test_load_pep(self):
        self.assertEqual(self.pep.pep_text,
                         PEP.load_pep(8, directory='pep_documents').pep_text)

    def test_pep_text(self):
        self.assertIsNotNone(self.pep.pep_text)
        lines = self.pep.pep_text.splitlines()
        for line in lines:
            self.assertTrue(isinstance(line, str))

    def test_pep_parse_title(self):
        self.pep.parse_metadata()

        self.assertEqual('Style Guide for Python Code',
                         self.pep.title)

    def test_pep_parse_number(self):
        self.pep.parse_metadata()
        self.assertEqual('8', self.pep.number)

    def test_pep_parse_authors(self):
        self.pep.parse_metadata()
        authors = ['Guido van Rossum <guido@python.org>',
                   'Barry Warsaw <barry@python.org>',
                   'Nick Coghlan <ncoghlan@gmail.com>']
        self.assertTrue(isinstance(self.pep.authors, list))
        self.assertEqual(authors, self.pep.authors)

    def test_pep_parse_type(self):
        self.pep.parse_metadata()
        self.assertEqual('Process', self.pep.type)

    def test_pep_parse_status(self):
        self.pep.parse_metadata()
        self.assertEqual('Active', self.pep.status)

    def test_pep_to_dict(self):
        self.pep.parse_metadata()
        pep_dict = self.pep.to_dict()
        self.assertIsInstance(pep_dict, dict)


if __name__ == '__main__':
    unittest.main()
