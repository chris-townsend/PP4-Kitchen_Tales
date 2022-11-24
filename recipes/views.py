from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Recipe, Comment
from .forms import CommentForm


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
    This view is used to display the full recipe details and comment section
    """
    def get(self, request, slug):
        """
        Retrives the recipe from the database
        """
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(
            approved=True).order_by('created_date')
        liked = False
        if recipe.like_recipe.filter(id=self.request.user.id).exists():
            liked = True
        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "comment_form": CommentForm(),
                "liked": liked,
            },
        )

    def post(self, request, slug):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(
            approved=True).order_by("-created_date")
        liked = False
        if recipe.like_recipe.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post_id = recipe.id
            comment.save()
            messages.success(
                self.request, 'Your comment is awaiting approval')
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked,
            },
        )


class RecipeLike(View):
    """This view is used to star a recipe and save it to the database"""
    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.like_recipe.filter(id=request.user.id).exists():
            recipe.like_recipe.remove(request.user)
        else:
            recipe.like_recipe.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))
