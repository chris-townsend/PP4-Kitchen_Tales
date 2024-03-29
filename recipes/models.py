from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField
from cloudinary.models import CloudinaryField
from django.urls import reverse


STATUS = ((0, "Draft"), (1, "Published"))


class Recipe(models.Model):
    """Model for adding recipes to the database"""
    title = models.CharField(max_length=48, unique=True,
                             null=False, blank=False)
    slug = AutoSlugField(populate_from='title', unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='recipe_posts')
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(default='A description about the recipe')
    prep_time = models.CharField(max_length=8, default='0 mins')
    cook_time = models.CharField(max_length=8, default='0 mins')
    ingredients = models.TextField()
    method = models.TextField()
    notes = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    image_url = models.URLField(blank=True)
    status = models.IntegerField(choices=STATUS, default=1)
    like_recipe = models.ManyToManyField(
        User, related_name='recipe_likes', default=None, blank=True)

    """Orders the recipes by created date"""
    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        """Gets the URL after a recipe has been added"""
        return reverse('recipe_detail', kwargs={'slug': self.slug})

    def number_of_saves(self):
        return self.save_recipe.count()


class Comment(models.Model):
    """Model for adding comments to the database"""
    post = models.ForeignKey(Recipe,
                             on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    name = models.CharField(max_length=70)
    email = models.EmailField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    """Orders the comments by created date"""
    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class NewsletterUser(models.Model):
    """Model used for adding a users email address to the database
        to signup to the newsletter"""
    email = models.EmailField(null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
