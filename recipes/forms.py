from .models import Comment, Recipe, NewsletterUser
from django import forms
from django_summernote.widgets import SummernoteWidget


class NewsletterForm(forms.ModelForm):
    """Create a newsletter form"""

    class Meta:
        """Retrieve the NewsletterUser model and display the 'email' field"""
        model = NewsletterUser
        fields = ('email',)


class CommentForm(forms.ModelForm):
    """Create a comment form"""

    class Meta:
        """Retrieve the Comment model and display the 'body' field"""
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    """Create a recipe form"""

    class Meta:
        """Retrieve the Recipe model and display the following fields"""
        model = Recipe
        fields = (
            'title',
            'prep_time',
            'cook_time',
            'description',
            'ingredients',
            'method',
            'notes',
            'image',
            'status',
        )
        """Display ingredients, method & notes using Summernote"""
        widgets = {
            'ingredients': SummernoteWidget(),
            'method': SummernoteWidget(),
            'notes': SummernoteWidget(),
        }
