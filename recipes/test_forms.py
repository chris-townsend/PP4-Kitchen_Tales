from django.test import TestCase
from .forms import RecipeForm, CommentForm, NewsletterForm

""" Unit testing for forms """


class TestForms(TestCase):
    """
    Testing for forms
    """
    def test_recipe_title_is_required(self):
        """
        Test to ensure recipe title is required
        """
        form = RecipeForm(({'title': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')
