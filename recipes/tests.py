from django.test import TestCase
from django.contrib.auth.models import User


class UserTests(TestCase):

    def test_register_page_load(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)
