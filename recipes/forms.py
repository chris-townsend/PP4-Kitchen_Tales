from .models import Comment, Recipe
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):

    class Meta:
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

        widgets = {
            'ingredients': SummernoteWidget(),
            'method': SummernoteWidget(),
            'notes': SummernoteWidget(),
        }
