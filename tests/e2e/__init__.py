"""Functional Tests"""


from app import app
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


if __name__ == '__main__':
    unittest.main()
