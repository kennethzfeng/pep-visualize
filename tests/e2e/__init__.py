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
            raw_content = f.read().decode('utf-8')
            pep = PEP(raw_content)
        if pep:
            pep.parse_metadata()
            pep_dict = pep.to_dict()
        self.assertDictEqual(json_obj['data'], pep_dict)
        self.assertEqual(json_obj['raw'], raw_content)

    def test_list_of_valid_peps(self):
        response = self.app.get('/pep')
        self.assertEqual(200, response.status_code)
        json_obj = json.loads(response.data, encoding='utf-8')
        self.assertIn('data', json_obj)
        self.assertIsInstance(json_obj['data'], list)
        self.assertIn(8, json_obj['data'])

    def test_error(self):
        response = self.app.get('/pep/-1')
        self.assertEqual(404, response.status_code)
        self.assertEqual('application/json', response.headers['Content-Type'])

    def test_invalid_pep_number_string_request(self):
        response = self.app.get('/pep/hello')
        self.assertEqual(404, response.status_code)
        self.assertEqual('application/json', response.headers['Content-Type'])

    def test_invalid_pep_number_request(self):
        response = self.app.get('/pep/99')
        self.assertEqual(404, response.status_code)
        self.assertEqual('application/json', response.headers['Content-Type'])


if __name__ == '__main__':
    unittest.main()
