import unittest

import requests


class PartnerIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.url = "http://localhost:8000/api/partner/upload/"
        self.files = {"file": open("assets/exemplo.csv", "rb")}

    def test_should_return_created_if_a_valid_csv_is_provider(self):
        respose = requests.post(self.url, files=self.files)
        self.assertEqual(respose.status_code, 201)
