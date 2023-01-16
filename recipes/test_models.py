from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
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
        recipe = Recipe.objects.create(title='Recipe test')
        self.assertEqual(str(Title), 'Recipe test')
