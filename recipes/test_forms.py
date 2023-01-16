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

    def test_recipe_description_is_required(self):
        """
        Test to ensure recipe description is required
        """
        form = RecipeForm(({'description': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors['description'][0],
                         'This field is required.')

    def test_recipe_ingredients_is_required(self):
        """
        Test to ensure recipe ingredients are required
        """
        form = RecipeForm(({'ingredients': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('ingredients', form.errors.keys())
        self.assertEqual(form.errors['ingredients'][0],
                         'This field is required.')

    def test_recipe_method_is_required(self):
        """
        Test to ensure recipe method is required
        """
        form = RecipeForm(({'method': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('method', form.errors.keys())
        self.assertEqual(form.errors['method'][0],
                         'This field is required.')

    def test_recipe_notes_is_required(self):
        """
        Test to ensure recipe notes are required
        """
        form = RecipeForm(({'notes': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('notes', form.errors.keys())
        self.assertEqual(form.errors['notes'][0],
                         'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Test to ensure fields listed in the meta class are present
        """
        form = RecipeForm()
        self.assertEqual(form.Meta.fields, (
            'title', 'prep_time', 'cook_time', 'description', 'ingredients',
            'method', 'notes', 'image', 'status'))
