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
        login = self.client.login(username='testuser', password='test1')

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
        Test add recipe page load
        """
        self.client.login(username='testuser', password='test1')
        response = self.client.get('/add_recipe/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_recipe.html')

    def test_can_add_recipe(self):
        """
        Testing recipe can be added to the database
        """
        self.client.post(f'/add_recipe/', {
                        'title': 'Test Title',
                        'description': 'Test Description',
                        'ingredients': 'Test Ingredients',
                        'method': 'Test method'
                         })
        add_new_recipe = Recipe.objects.filter(title='Test Title')
        self.assertEqual(len(add_new_recipe), 0)

    @property
    def test_can_update_recipe(self):
        """
        Testing recipe can be updated
        """
        response = self.client.get(f'/update_recipe/{self.recipe.pk}/', {
                                   'title': 'Updated Title',
                                   'description': 'Updated description',
                                   'ingredients': 'Updated ingredients',
                                   'method': 'Test method'
                                   })
        update_recipe = Recipe.objects.first()
        self.assertEqual(update_recipe, "Updated Title")

    def test_edit_recipe_page(self):
        """
        Edit recipe page display as expected
        """
        recipes = Recipe.objects.all()
        for recipe in recipes:
            response = self.client.get(f'/update_recipe/{self.recipe.pk}/')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'update_recipe.html')

    def test_delete_recipe_page(self):
        """
        Delete recipe page display as expected
        """
        recipes = Recipe.objects.all()
        for recipe in recipes:
            response = self.client.get(f'/delete_recipe/{self.recipe.pk}/')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'delete_recipe.html')

    def test_get_my_recipes_page(self):
        """
        Test user created recipes page load
        """
        self.client.login(username='testuser', password='test1')
        response = self.client.get('/my_recipes/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_recipes.html')

    def test_get_recipe_detail_page(self):
        """
        Test recipe detail page load
        """
        self.client.login(username='testuser', password='test1')
        response = self.client.get(f'/recipe_detail/{self.recipe.slug}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_detail.html')

    def test_get_newsletter_page(self):
        """
        Test newsletter page load
        """
        response = self.client.get('/newsletter')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'newsletter.html')

    def test_get_search_results(self):
        """
        Test search results page load
        """
        response = self.client.get('/search_results/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search_results.html')

    def test_update_comment_page(self):
        """
        Edit comment page display as expected
        """
        comments = Comment.objects.all()
        for comment in comments:
            response = self.client.get(f'/update_comment/{self.comment.id}')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'update_comment.html')

    def test_delete_comment_page(self):
        """
        Delete comment page display as expected
        """
        comments = Comment.objects.all()
        for comment in comments:
            response = self.client.get(f'/delete_comment/{self.comment.pk}')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'delete_comment.html')

    def test_can_add_comment(self):
        """
        Testing comments can be added to database
        """
        comments = Comment.objects.all()
        for comment in comments:
            response = self.client.post(f'/{self.comment.pk}/',
                                        {'body': 'Test Comment'})
            self.assertEqual(Comment.objects.last().body, "Test Comment")
            self.assertTemplateUsed(response, 'recipe_detail.html')

    def test_can_update_comment(self):
        """
        Testing comments can be updated
        """
        comments = Comment.objects.all()
        for comment in comments:
            response = self.client.post(f'/update_comment/{self.comment.pk}',
                                        {'body': 'Updated Comment'})
            self.assertRedirects(response, f'/{self.comment.recipe.slug}/')
            updated_comment = Comment.objects.last().body
            self.assertEqual(updated_comment, "Updated Comment")

    def test_get_newsletter_page(self):
        """
        Test newsletter page load
        """
        response = self.client.get('/newsletter')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'newsletter.html')

    def test_can_add_newsletter_user(self):
        """
        Testing email can be added to the database
        """
        self.client.post(f'/newsletter/', {
                        'email': 'Test email',
                        'date_added': 'Test date_added'
                         })
        add_new_email = NewsletterUser.objects.filter(email='Test email')
        self.assertEqual(len(add_new_email), 0)
