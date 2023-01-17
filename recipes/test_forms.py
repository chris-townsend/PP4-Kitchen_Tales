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

    def test_fields_are_explicit_in_recipe_form_metaclass(self):
        """
        Test to ensure fields listed in the meta class are present
        """
        form = RecipeForm()
        self.assertEqual(form.Meta.fields, (
            'title', 'prep_time', 'cook_time', 'description', 'ingredients',
            'method', 'notes', 'image', 'status'))

    def test_field_is_explicit_in_comment_form_metaclass(self):
        """
        Test to ensure the body field is listed in the meta class
        """
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('body',))

    def test_comment_body_is_required(self):
        """
        Test to ensure comment body is required
        """
        form = CommentForm(({'body': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0],
                         'This field is required.')

    def test_newsletter_email_is_required(self):
        """
        Test to ensure newsletter email address is required
        """
        form = NewsletterForm(({'email': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0],
                         'This field is required.')

    def test_fields_are_explicit_in_newsletter_form_metaclass(self):
        """
        Test to ensure fields listed in the meta class
         are present for the Newsletter
        """
        form = NewsletterForm()
        self.assertEqual(form.Meta.fields, ('email',))
