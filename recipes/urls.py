from django.urls import path
from . import views
from .views import (RecipeListHome, AddRecipeView,
                    UpdateRecipeView, DeleteRecipeView, RecipeLike,
                    DeleteCommentView, UpdateCommentView, newsletter_signup)


""" URL Patterns """

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path('all_recipes/', views.RecipeListHome.as_view(), name='all_recipes'),
    path('recipe_detail/<slug:slug>/', views.RecipeDetail.as_view(),
         name='recipe_detail'),
    path('like/<slug:slug>/', views.RecipeLike.as_view(), name='recipe_like'),
    path('add_recipe/', AddRecipeView.as_view(), name='add_recipe'),
    path('update_recipe/<int:recipe_id>/', UpdateRecipeView.as_view(),
         name='update_recipe'),
    path('delete_recipe/<int:pk>/', DeleteRecipeView.as_view(),
         name='delete_recipe'),
    path('my_recipes/', views.MyRecipesView.as_view(), name='my_recipes'),
    path('my_starred_recipes/', views.MyStarredRecipesView.as_view(),
         name='save_recipe'),
    path('search_results/', views.search_results, name='search_result'),
    path('delete_comment/<int:pk>/', DeleteCommentView.as_view(),
         name='delete_comment'),
    path('update_comment/<int:comment_id>/', UpdateCommentView.as_view(),
         name='update_comment'),
    path("newsletter", views.newsletter_signup, name="newsletter"),
]
