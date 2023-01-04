from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Recipe, Comment, NewsletterUser


class TestModels(TestCase):

    # Create two test users who are logged in for unit tests
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',
                                             password='test1')
        login = self.client.login(username='testuser', password='test')

    # testing page load in recipe app
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_all_recipes_status_code(self):
        response = self.client.get('/all_recipes/')
        self.assertEqual(response.status_code, 200)

    def test_register_page_templates_load(self):
        response = self.client.get('/signup/')
        self.assertTemplateUsed(response, "base.html")

    def test_login_page_templates_load(self):
        response = self.client.get('/login/')
        self.assertTemplateUsed(response, "base.html")

    def test_logout_page_templates_load(self):
        response = self.client.get('/logout/')
        self.assertTemplateUsed(response, "base.html")
