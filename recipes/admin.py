from django.contrib import admin
from .models import Recipe
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """Admin can manage recipes within the Django admin panel """
    list_filter = ('status', 'created_date')
    list_display = ('title', 'slug', 'status', 'created_date')
    search_fields = ('title', 'method', 'notes', 'ingredients')
    summernote_fields = ('ingredients', 'method', 'notes')
