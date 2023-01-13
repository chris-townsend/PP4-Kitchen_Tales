from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Recipe, Comment, NewsletterUser


class TestViews(TestCase):

    def setUp(self):
        """
        Setup a test user for testing views
        """
        user = User.objects.create_user(username='testuser',
                                        password='test1')
        self.recipe = Recipe.objects.create(title='Test', author=user)
        login = self.client.login(username='testuser', password='test')

    def testLogin(self):
        """
        Test login works
        """
        self.client.login(username='testuser', password='test1')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_status_code(self):
        """
        Test homepage loads
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_all_recipes_status_code(self):
        """
        Test all_recipes page loads
        """
        response = self.client.get('/all_recipes/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'all_recipes.html')

    def test_register_page_templates_load(self):
        """
        Test register page loads
        """
        response = self.client.get('/signup/')
        self.assertTemplateUsed(response, "base.html")

    def test_login_page_templates_load(self):
        """
        Test login page loads
        """
        response = self.client.get('/login/')
        self.assertTemplateUsed(response, "base.html")

    def test_logout_page_templates_load(self):
        """
        Test logout page loads
        """
        response = self.client.get('/logout/')
        self.assertTemplateUsed(response, "base.html")

    def test_get_add_recipes_page(self):
        """
        Test to ensure add recipes page is displayed
        """
        self.client.login(username='testuser', password='test1')
        response = self.client.get('/add_recipe/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_recipe.html')

    def test_get_my_recipes_page(self):
        """
        Test to ensure your recipes page is displayed
        """
        self.client.login(username='testuser', password='test1')
        response = self.client.get('/my_recipes/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_recipes.html')

    def test_get_recipe_detail_page(self):
        """
        Test to ensure recipe detail page is displayed
        """
        self.client.login(username='testuser', password='test1')
        response = self.client.get(f'/recipe_detail/{self.recipe.slug}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_detail.html')

    def test_get_update_recipes_page(self):
        self.client.login(username='testuser', password='test1')
        response = self.client.get(f'/update_recipe/{self.recipe.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_recipe.html')
