from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Recipe


class Home(generic.TemplateView):
    template_name = 'index.html'


class RecipeListHome(generic.ListView):
    """
    This view is used to display all recipes in the all recipes page
    """
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_date')
    template_name = 'all_recipes.html'
    paginate_by = 8


class RecipeDetail(View):
    """
    This view is used to display the full recipe details
    """
    def get(self, request, slug):
        """
        Retrives the recipe from the database
        """
        queryset = Recipe.objects.all()
        recipe = get_object_or_404(queryset, slug=slug)
        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
            },
        )
