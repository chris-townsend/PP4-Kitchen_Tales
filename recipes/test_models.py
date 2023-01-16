from django.test import TestCase
from django.contrib.auth.models import User
from .models import Recipe, Comment, NewsletterUser

""" Unit testing for models """


class TestModels(TestCase):
    """
    Testing for models
    """
    def test_recipe_model_str(self):
        """
        Testing when calling the string method, it returns the correct string
        """
        recipe = Recipe(title='Test Recipe')
        self.assertEqual(str(recipe), recipe.title)

    def test_comment_model_str(self):
        """
        Testing when calling the string method, it returns the correct string
        """
        comment = Comment(body='Test Comment',
                          name='testuser'
                          )
        self.assertEqual(str(comment), 'Comment Test Comment by testuser')
