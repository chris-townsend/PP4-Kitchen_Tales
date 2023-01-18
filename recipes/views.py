from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import Recipe, Comment, NewsletterUser
from .forms import CommentForm, RecipeForm, NewsletterForm


def newsletter_signup(request):
    """
    This function allows a user to sign up to the newsletter,
    if a valid email address is input, the email will save to the
    database and a success message notifying the user.
    """
    newsletter_form = NewsletterForm()
    if request.method == 'POST':
        newsletter_form = NewsletterForm(request.POST)
        print(newsletter_form)
        if newsletter_form.is_valid():
            newsletter_form.save()
            messages.success(request,
                             'You have successfully subscribed')
            return redirect('home')
        else:
            messages.error(request, "Request failed")
    else:
        newsletter_form = NewsletterForm()

    context = {
            'form': newsletter_form,
             }

    return render(request, 'newsletter.html', context)


def search_results(request):
    """
    The search_results function is used to search for a recipe
    """
    if request.method == "POST":
        """
        When a POST request is made this method is called which
        renders the search results based on recipe title
        """
        searched = request.POST['searched']
        results = Recipe.objects.filter(title__contains=searched)

        return render(request, 'search_results.html',
                      {'searched': searched,
                       'results': results})
    else:
        return render(request, 'search_results.html',)


class Home(generic.TemplateView):
    """
    The main homepage view for the site
    """
    template_name = 'index.html'


class RecipeListHome(generic.ListView):
    """
    This view is used to display all recipes in the main recipes page
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
        """
        When a POST request is made to this view from
        the comments section this method is called
        """
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


class RecipeLike(LoginRequiredMixin, View):
    """
    This view is used to star a recipe and save it to the database,
    success messages used to alert the user
    """
    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.like_recipe.filter(id=request.user.id).exists():
            recipe.like_recipe.remove(request.user)
            messages.success(
                self.request,
                'Recipe removed from your saved-Recipes'
                '<i class="far fa-star"></i>')
        else:
            recipe.like_recipe.add(request.user)
            messages.success(
                self.request,
                'Recipe saved! Find it in your saved-Recipes'
                '<i class="far fa-star"></i>')

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


class AddRecipeView(LoginRequiredMixin, generic.CreateView):
    """
    This view allows a logged-in user to add a recipe to the site
    """
    model = Recipe
    form_class = RecipeForm
    template_name = 'add_recipe.html'

    def post(self, request):
        """
        This method is called when a POST request is made to the view,
        a success message will alert the user of a successful add
        of a new recipe
        """
        recipe_form = RecipeForm(data=request.POST)

        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = User.objects.get(id=request.user.id)
            recipe.image = request.FILES.get('image')
            recipe.save()
            messages.success(
                self.request,
                'Your recipe has been added successfully')

            return redirect(reverse('recipe_detail', args={recipe.slug}))

        else:
            messages.error(self.request, 'Please complete all required fields')
            recipe_form = RecipeForm()

            return render(
                request,
                "add_recipe.html",
                {
                    "form": RecipeForm,
                },
            )


class UpdateRecipeView(LoginRequiredMixin, View):
    """
    This view allows a logged-in user to edit their own recipe
    """
    model = Recipe
    form_class = RecipeForm
    template_name = 'update_recipe.html'

    def get(self, request, recipe_id):
        """
        Gets the recipe from the database and returns the data
        within the form
        """
        recipe = Recipe.objects.get(id=recipe_id)
        print(recipe)
        return render(
            request,
            "update_recipe.html",
            {
                "form": RecipeForm(instance=recipe),
                "recipe": recipe
            },
        )

    def post(self, request, recipe_id):
        """
        The form is posted with the updated data if the RecipeForm
        data is valid and a success message is displayed to the user
        """
        recipe = Recipe.objects.get(id=recipe_id)
        recipe_form = RecipeForm(request.POST, instance=recipe)

        if recipe_form.is_valid():
            recipe.image = request.FILES.get('image')
            recipe_form.save()
            messages.success(
                self.request,
                'Your recipe has been updated')

        return redirect(reverse('recipe_detail', args={recipe.slug}))


class DeleteRecipeView(LoginRequiredMixin, generic.DeleteView):
    """
    This view allows a logged-in user to delete their own recipe
    from the database
    """
    model = Recipe
    template_name = 'delete_recipe.html'
    success_url = reverse_lazy('my_recipes')
    success_message = 'Your recipe has been removed from the database'

    def delete(self, request, *args, **kwargs):
        """
        delete function is used to display success message
        """
        messages.success(self.request, self.success_message)
        return super(DeleteRecipeView, self).delete(request, *args, **kwargs)


class DeleteCommentView(LoginRequiredMixin, generic.DeleteView):
    """
    This view allows a logged-in user to delete their own comment
    """
    model = Comment
    template_name = 'delete_comment.html'
    success_url = reverse_lazy('my_recipes')
    success_message = 'Your comment has been removed'

    def delete(self, request, *args, **kwargs):
        """
        delete function is used to display success message
        """
        messages.success(self.request, self.success_message)
        return super(DeleteCommentView, self).delete(request, *args, **kwargs)


class MyRecipesView(LoginRequiredMixin, generic.ListView):
    """
    This view is used to display a logged-in user created recipes
    """
    model = Recipe
    template_name = 'my_recipes.html'
    paginate_by = 8

    def get_queryset(self):
        """
        Display results by author
        """
        return Recipe.objects.filter(author=self.request.user)


class MyStarredRecipesView(LoginRequiredMixin, generic.ListView):
    """
    This view is used to display a logged-in user starred recipes
    """
    model = Recipe
    template_name = 'my_starred_recipes.html'
    paginate_by = 8

    def get_queryset(self):
        return Recipe.objects.filter(like_recipe=self.request.user.id)


class UpdateCommentView(LoginRequiredMixin, View):
    """
    This view allows a logged-in user to edit their own comment
    """
    model = Comment
    form_class = CommentForm
    template_name = 'update_comment.html'

    def get(self, request, comment_id):
        """
        retrieves the comment from the database
        and displays a form to edit the comment
        """
        comment = Comment.objects.get(id=comment_id)
        print(comment)
        return render(
            request,
            "update_comment.html",
            {
                "form": CommentForm(instance=comment),
                "comment": comment
            },
        )

    def post(self, request, comment_id):
        """
        If valid data has been input by the user, the comment
        will be updated and the user alerted with a success message
        and returned back to the main recipes page
        """
        comment = Comment.objects.get(id=comment_id)
        comment_form = CommentForm(request.POST, instance=comment)

        if comment_form.is_valid():
            comment_form.save()
            messages.success(
                self.request,
                'Your comment has been updated')

        return redirect(reverse('recipe_detail', args={comment.post.slug}))
