"""Functional Tests"""


from app import app
from app.models import PEP
import unittest
import json


class APITest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_get_pep(self):
        response = self.app.get('/pep/8')
        self.assertEqual(200, response.status_code)
        json_obj = json.loads(response.data, encoding='utf-8')
        self.assertIn('data', json_obj)

        with open('pep_documents/pep-0008.txt', 'rb') as f:
            pep = PEP(f.read().decode('utf-8'))
        if pep:
            pep.parse_metadata()
            pep_dict = pep.to_dict()
        self.assertDictEqual(json_obj['data'], pep_dict)


if __name__ == '__main__':
    unittest.main()
