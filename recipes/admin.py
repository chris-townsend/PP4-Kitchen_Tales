from django.contrib import admin
from .models import Recipe
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """Admin can manage recipes within the Django admin panel """

    summernote_fields = ('ingredients', 'method', 'notes')
