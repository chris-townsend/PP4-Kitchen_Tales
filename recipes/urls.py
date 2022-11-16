from . import views
from django.urls import path

"""URL Patterns"""

urlpatterns = [
    path("", views.RecipeList.as_view(), name="home"),
]
