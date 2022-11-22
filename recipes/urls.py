from . import views
from django.urls import path
from .views import RecipeListHome

"""URL Patterns"""

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path('all_recipes/', views.RecipeListHome.as_view(), name='all_recipes'),
    path('recipe_detail/<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>/', views.RecipeLike.as_view(), name='recipe_like')
]
