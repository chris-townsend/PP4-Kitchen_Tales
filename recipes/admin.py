from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """Admin can manage recipes within the Django admin panel """
    list_filter = ('status', 'created_date')
    list_display = ('title', 'slug', 'status', 'created_date')
    search_fields = ('title', 'method', 'notes', 'ingredients')
    summernote_fields = ('ingredients', 'method', 'notes')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_date', 'approved')
    list_filter = ('approved', 'created_date')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

