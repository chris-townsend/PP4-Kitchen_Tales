from django.contrib import admin
from .models import Recipe, Comment, NewsletterUser
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """
    Admin can manage recipes within the Django admin panel
    """
    list_filter = ('status', 'created_date')
    list_display = ('title', 'slug', 'status', 'created_date')
    search_fields = ('title', 'method', 'notes', 'ingredients')
    summernote_fields = ('ingredients', 'method', 'notes')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin can manage comments on a recipe_detail page within the admin panel
    """
    list_display = ('name', 'body', 'post', 'created_date', 'approved')
    list_filter = ('approved', 'created_date')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


class NewsletterAdmin(admin.ModelAdmin):
    """
    Displays a users email address and the date they subscribed
    to the newsletter within the admin panel
    """

    list_display = ('email', 'date_added')

    admin.site.register(NewsletterUser)
