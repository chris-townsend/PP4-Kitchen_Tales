from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField
from cloudinary.models import CloudinaryField
from django.urls import reverse

STATUS = ((0, "Draft"), (1, "Published"))


class Recipe(models.Model):
    """Model for adding recipes to the database"""
    title = models.CharField(max_length=48, unique=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipe_posts')
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    prep_time = models.CharField(max_length=6, default=0)
    cook_time = models.CharField(max_length=6)
    ingredients = models.TextField()
    method = models.TextField()
    notes = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    like_recipe = models.ManyToManyField(
        User, related_name='recipe_likes', default=None, blank=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        # Returns back to the recipe detail page which the user just created
        return reverse('recipe_detail', kwargs={'slug': self.slug})
     
    def number_of_saves(self):
        return self.save_recipe.count()


class Comment(models.Model):
    """Model for adding comments to the database"""
    post = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    name = models.CharField(max_length=70)
    email = models.EmailField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
